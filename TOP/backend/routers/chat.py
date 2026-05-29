# routers/chat.py
import re
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
from services.llm_service import chat_with_model
from services.word_service import fill_template
from services.session_store import get_history, add_message, clear_session

router = APIRouter(prefix="/api", tags=["chat"])

SYSTEM_PROMPT = """你是一位專業的客服助理。
你的任務是根據資料回答客戶的問題，但目前沒有資料所以自由發揮，如果客戶有意願要購買透過對話，依序蒐集以下資訊：

1. 客戶姓名
2. 客戶聯絡方式（電話）
3. 想要的服務內容
4. 期望日期
5. 顏色喜好
6. 備註（若無請填無）

注意事項：
- 每次只問一個問題，不要一次問全部
- 用親切友善的語氣
- 確認所有資訊蒐集完畢後，輸出以下區塊：

<<<DATA>>>
{
  "name": "客戶姓名",
  "phone": "電話號碼",
  "service": "想要的服務",
  "date": "期望日期",
  "color": "顏色喜好",
  "note": "備註"
}
<<<END>>>

請用繁體中文回答。"""


# ── 工具函式 ──────────────────────────────────────────

def extract_data(reply: str) -> dict | None:
    match = re.search(r'<<<DATA>>>(.*?)<<<END>>>', reply, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            return None
    return None


def clean_reply(reply: str) -> str:
    return re.sub(r'<<<DATA>>>.*?<<<END>>>', '', reply, flags=re.DOTALL).strip()


# ── Schema ────────────────────────────────────────────

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


# ── Endpoints ─────────────────────────────────────────

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # 記錄使用者訊息
    add_message(request.session_id, "user", request.message)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *get_history(request.session_id),
    ]

    try:
        raw_reply = await chat_with_model(messages)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    # 記錄 LLM 回覆
    add_message(request.session_id, "assistant", raw_reply)

    collected = extract_data(raw_reply)
    if collected:
        fill_template(collected, request.session_id)
        clear_session(request.session_id)  # 蒐集完清掉記憶體

    return ChatResponse(
        reply=clean_reply(raw_reply),
        session_id=request.session_id,
        collected=collected,
    )


@router.get("/health")
async def health_check():
    return {"status": "ok"}