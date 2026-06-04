# AI 客服系統

以 FastAPI + Ollama 本地模型為核心的客服對話系統，透過對話自動蒐集客戶資訊並輸出成 Word 表單。

---

## 專案結構

```
backend/
├── output/                  # 自動產生的需求表單 Word 檔（.docx）
├── rag/
│   └── vectorstore/         # Chroma 向量資料庫（由 RAG 端提供，直接覆蓋放入）
├── routers/
│   └── chat.py              # 聊天 API 路由、SYSTEM_PROMPT、資料擷取邏輯
├── services/
│   ├── llm_service.py       # 呼叫 Ollama 模型
│   ├── rag_service.py       # 查詢向量資料庫
│   ├── session_store.py     # 對話歷史記憶體暫存
│   └── word_service.py      # 填寫並輸出需求表單
├── .gitignore
├── config.py                # 環境設定（模型名稱、port 等）
├── main.py                  # FastAPI 應用程式入口
├── requirements.txt         # Python 套件需求
└── template.docx            # 需求表單範本
```

---

## 環境需求

- Python 3.10+
- [Ollama](https://ollama.com/download) 已安裝並在本機執行

---

## 快速開始

### 1. 下載模型

確認 Ollama 已啟動後，下載模型：

```powershell
ollama pull gemma4-E4b-it-uncensored
```

### 2. 安裝相依套件

```bash
pip install -r requirements.txt
```

### 3. 設定環境變數

複製範例檔並修改 `.env`：

```bash
cp .env.example .env
```

主要設定項目：

| 設定 | 預設值 | 說明 |
|------|--------|------|
| `model_name` | `hf.co/TrevorJS/gemma-4-E4B-it-uncensored-GGUF:Q4_K_M` | Ollama 模型名稱 |
| `model_base_url` | `http://127.0.0.1:11434` | Ollama 服務位址 |
| `app_host` | `127.0.0.1` | 服務綁定 IP |
| `app_port` | `8000` | 服務埠號 |

### 4. 放入向量資料庫

將 RAG 端提供的 `vectorstore/` 資料夾覆蓋放入 `rag/` 目錄下：

```
backend/rag/vectorstore/   ← 放在這裡
```

### 5. 啟動服務

```bash
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

服務啟動後開啟：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 需求表單欄位說明

表單由三個部分組成，欄位、佔位符、SYSTEM_PROMPT 三者必須保持同步：

### 客戶基本資料

| 欄位顯示名稱 | 佔位符 | SYSTEM_PROMPT 對應項目 |
|-------------|--------|----------------------|
| 客戶姓名 | `{{name}}` | 客戶姓名 |
| 公司／單位名稱 | `{{company}}` | 公司／單位名稱 |
| 聯絡電話 | `{{phone}}` | 聯絡電話 |
| 電子郵件 | `{{email}}` | 電子郵件 |
| 來源管道 | `{{source}}` | 來源管道 |

### 需求內容

| 欄位顯示名稱 | 佔位符 | SYSTEM_PROMPT 對應項目 |
|-------------|--------|----------------------|
| 需求項目／服務類型 | `{{service}}` | 需求項目／服務類型 |
| 數量與預算範圍 | `{{quantity_budget}}` | 數量與預算範圍 |
| 規格需求 | `{{spec}}` | 規格需求，例如顏色喜好 |

### 其他資訊

| 欄位顯示名稱 | 佔位符 | 說明 |
|-------------|--------|------|
| 建立日期 | `{{created_date}}` | 由程式自動填入，不需 LLM 蒐集 |
| 補充說明 | `{{note}}` | 補充說明 |

---

## 修改需求表單的步驟

新增、刪除或修改欄位時，以下三個地方必須同步修改，缺一不可：

### 步驟一：修改 `template.docx`

在表單範本中新增或刪除對應列，佔位符格式為 `{{欄位名稱}}`。

> 建議使用原始腳本重新產生 `template.docx`，而非直接手動編輯，以避免格式跑版。

### 步驟二：修改 `routers/chat.py` 的 `SYSTEM_PROMPT`

在蒐集清單中新增或刪除對應項目，並同步更新 `<<<DATA>>>` 區塊的 JSON 範本：

```python
SYSTEM_PROMPT = """
...
二、依序蒐集以下資訊：
1. 客戶姓名
2. 新增的欄位名稱   ← 在這裡新增
...
<<<DATA>>>
{
  "name": "客戶姓名",
  "new_field": "新欄位內容",   ← 在這裡新增
  ...
}
<<<END>>>
"""
```

### 步驟三：修改 `services/word_service.py` 的 `defaults`

在 `fill_template` 函式的 `defaults` 字典中新增對應鍵值，避免佔位符殘留在表單上：

```python
defaults = {
    "name": "", "company": "", "phone": "", "email": "",
    "source": "", "service": "", "quantity_budget": "",
    "spec": "", "note": "",
    "new_field": "",          # ← 在這裡新增
    "created_date": data["created_date"]
}
```

---

## API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| `POST` | `/api/chat` | 主要聊天端點 |
| `GET` | `/api/health` | 服務健康檢查 |

### POST `/api/chat` 請求格式

```json
{
  "message": "使用者輸入的訊息",
  "session_id": "用來區分不同對話的識別碼（可自訂）"
}
```

### 回應格式

```json
{
  "reply": "AI 回覆內容",
  "session_id": "對話識別碼",
  "collected": null
}
```

> 當表單資料蒐集完畢，`collected` 會回傳填寫完成的 JSON 物件，同時在 `output/` 目錄產生 `.docx` 檔案。

---

## 常見問題

**Q：模型回應很慢怎麼辦？**

Ollama 預設 timeout 為 120 秒，本機跑大模型需要時間，屬正常現象。可在 `config.py` 更換較小的模型。

**Q：表單產生失敗怎麼辦？**

確認 `template.docx` 存在於專案根目錄（與 `main.py` 同層），且佔位符格式正確（雙大括號，例如 `{{name}}`）。

**Q：對話結束後歷史紀錄沒有清除？**

Session 歷史存在記憶體中，重啟服務會自動清除。表單蒐集完成後也會自動清除當前 session。

---

*最後更新：2026-06-03*