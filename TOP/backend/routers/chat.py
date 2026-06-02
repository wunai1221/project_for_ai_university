import re
import json
import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from services.llm_service import chat_with_model
from services.word_service import fill_template
from services.session_store import get_history, add_message, clear_session
from services.rag_service import search as rag_search

router = APIRouter(prefix="/api", tags=["chat"])

# 初始化 Logger，避免在生產環境直接使用 print 導致日誌難以追蹤
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """你是一位專業的客服助理。

你的任務有兩個：

一、根據「參考資料」回答客戶問題
- 優先根據參考資料回答。
- 如果參考資料不足以回答，請誠實告知「目前資料中沒有明確資訊」。
- 不要編造不存在的公司資訊、價格、規格或承諾。
- 請用自然、親切、專業的繁體中文回答。

二、如果客戶有購買、詢價、預約、合作或進一步聯絡的意願，請透過對話依序蒐集以下資訊：

1. 客戶姓名
2. 公司／單位名稱（若無請填無）
3. 聯絡電話
4. 電子郵件（若無請填無）
5. 來源管道（如何得知我們，例如官網、Line、朋友介紹等）
6. 需求項目／服務類型
7. 數量與預算範圍（若無請填無）
8. 規格需求，例如顏色喜好（若無請填無）
9. 期望日期
10. 負責業務姓名（若不知道請填無）
11. 補充說明（若無請填無）

注意事項：
- 每次只問一個問題，不要一次問全部。
- 不要在資料還沒收集完整時輸出 DATA。
- 確認所有資訊蒐集完畢後，才輸出以下區塊：

<<<DATA>>>
{
  "name": "客戶姓名",
  "company": "公司／單位名稱",
  "phone": "聯絡電話",
  "email": "電子郵件",
  "source": "來源管道",
  "service": "需求項目／服務類型",
  "quantity_budget": "數量與預算範圍",
  "spec": "規格需求",
  "date": "期望日期",
  "staff": "負責業務",
  "note": "補充說明"
}
<<<END>>>

請用繁體中文回答。
"""


def extract_data(reply: str) -> dict | None:
    """從 LLM 回覆中擷取 <<<DATA>>> ... <<<END>>> 裡面的 JSON"""
    match = re.search(r"<<<DATA>>>(.*?)<<<END>>>", reply, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1).strip())
    except json.JSONDecodeError:
        logger.error(f"JSON 解析失敗，原始文字: {match.group(1)}")
        return None


def clean_reply(reply: str) -> str:
    """移除給後端使用的 DATA 區塊，避免顯示給使用者"""
    return re.sub(r"<<<DATA>>>.*?<<<END>>>", "", reply, flags=re.DOTALL).strip()


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

    @field_validator("message")
    @classmethod
    def message_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("訊息不能空白")
        if len(v) > 2000:
            raise ValueError("訊息過長，請限制在 2000 字以內")
        return v


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    collected: dict | None = None


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # 1. 查詢 RAG 向量資料庫
    try:
        context = rag_search(query=request.message, top_k=5)
    except Exception as e:
        logger.error(f"RAG 查詢失敗：{e}")
        context = ""

    # 2. 記錄使用者訊息到對話歷史
    add_message(request.session_id, "user", request.message)

    # 3. 動態組合當前這輪的 System Prompt (包含最新的 RAG 參考資料)
    system_with_context = SYSTEM_PROMPT
    if context:
        system_with_context += f"\n\n以下是參考資料，請優先根據這些內容回答：\n\n{context}"
    else:
        system_with_context += "\n\n目前沒有查詢到足夠的參考資料。如果使用者問題需要資料庫內容才能回答，請誠實告知目前資料不足。"

    # 4. 組合對話歷史
    messages = [
        {"role": "system", "content": system_with_context},
        *get_history(request.session_id),
    ]

    # 5. 呼叫 LLM
    try:
        raw_reply = await chat_with_model(messages)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    # 6. 【關鍵優化】先解析資料與清洗回覆，確保髒代碼不進入記憶
    collected = extract_data(raw_reply)
    final_reply = clean_reply(raw_reply)

    # 7. 【關鍵優化】記錄 AI 回覆：只記錄洗乾淨後的純對話文字
    add_message(request.session_id, "assistant", final_reply)

    # 8. 檢查是否已收集完成資料並處理
    if collected:
        try:
            fill_template(collected, request.session_id)
        except Exception as e:
            logger.error(f"Word 產生失敗：{e}")
        
        # 清除當前 Session 歷史紀錄
        clear_session(request.session_id)
        logger.info(f"Session {request.session_id} 表單收集完畢，已清空歷史紀錄並產出需求單。")

    # 9. 回傳乾淨回覆與收集到的資料給前端
    return ChatResponse(
        reply=final_reply,
        session_id=request.session_id,
        collected=collected,
    )


@router.get("/health")
async def health_check():
    return {"status": "ok"}