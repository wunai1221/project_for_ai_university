# 鉅昕鋼鐵 AI 客服系統

鉅昕鋼鐵股份有限公司的 AI 客服聊天機器人專案，結合 RAG 向量檢索與本地 LLM，透過對話自動回答客戶問題並蒐集需求資訊，最終輸出成 Word 需求表單。

---

## 系統架構

```
使用者
  │
  ▼
前端網站（React）
  │  POST /api/chat
  ▼
後端 API（FastAPI）
  ├── RAG 向量查詢 ──→ Chroma 向量資料庫
  ├── LLM 推論 ──────→ Ollama 本地模型
  └── 輸出需求表單 ──→ output/*.docx
```

---

## 專案結構

```
TOP/
├── frontend/        # React + TypeScript 前端網站
├── backend/         # FastAPI 後端 + LLM 串接 + 表單輸出
└── rag/             # RAG 資料管道與向量資料庫建構
```

---

## 分工說明

| 模組 | 負責內容 |
|------|----------|
| `frontend/` | 網站頁面、產品展示、AI 客服聊天視窗 |
| `backend/` | FastAPI API、Ollama 模型串接、對話邏輯、需求表單輸出 |
| `rag/` | 資料收集清洗、JSON 格式化、向量化、Chroma 資料庫建構 |

---

## 快速開始

各模組有各自的啟動說明，請依序參考：

1. **RAG**：先建立向量資料庫 → 詳見 [`rag/README.md`](rag/README.md)
2. **Backend**：啟動後端 API 服務 → 詳見 [`backend/README.md`](backend/README.md)
3. **Frontend**：啟動前端網站 → 詳見 [`frontend/README.md`](frontend/README.md)

---

## 環境需求總覽

| 項目 | 版本需求 |
|------|----------|
| Python | 3.10+ |
| Node.js | 18+ |
| Bun | 1.0+ |
| Ollama | 最新版 |

---

## 資料流說明

### 建置階段（RAG）

```
原始資料（官網爬蟲、PPT、Word、手動整理）
  │
  ▼
JSON 格式化（data/raw/）
  │
  ▼
build_vectorstore.py 向量化
  │
  ▼
Chroma 向量資料庫（vectorstore/）
  │
  ▼
複製至 backend/rag/vectorstore/
```

### 對話階段（Runtime）

```
使用者輸入
  │
  ▼
RAG 查詢最相關的 5 筆參考資料
  │
  ▼
組合 System Prompt + 參考資料 + 對話歷史
  │
  ▼
Ollama 本地模型推論
  │
  ├─→ 一般問答：直接回覆
  │
  └─→ 有購買意願：依序蒐集客戶資訊
                    │
                    ▼
              蒐集完畢後輸出 Word 需求表單
```

---

## 模型資訊

| 項目 | 內容 |
|------|------|
| 模型 | Gemma 4 4B（非審查版） |
| 執行方式 | Ollama 本地執行 |
| 模型標籤 | `hf.co/TrevorJS/gemma-4-E4B-it-uncensored-GGUF:Q4_K_M` |
| Embedding 模型 | `paraphrase-multilingual-MiniLM-L12-v2` |

---

## 輸出說明

需求表單蒐集完畢後，系統會在 `backend/output/` 自動產生 `.docx` 檔案，檔名格式為：

```
ticket_{session_id}_{YYYYMMDD_HHMMSS}.docx
```

表單包含以下欄位：客戶姓名、公司/單位、聯絡電話、電子郵件、來源管道、需求項目、數量與預算、規格需求、補充說明、建立日期。

---

*最後更新：2026-06-03*
