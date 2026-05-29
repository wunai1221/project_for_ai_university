# API 介面規範（Frontend ↔ Backend）

> 本文件由 B 同學（Backend）主導填寫，A 同學（Frontend）與我（RAG）參考使用。
> 目前為初版草稿，細節待三人確認後更新。

---

## 問答 API

### 端點
```
POST /api/chat
```

### 請求格式（Frontend → Backend）
```json
{
  "question": "使用者輸入的問題",
  "session_id": "對話 session 識別碼（選填，用於多輪對話）"
}
```

### 回應格式（Backend → Frontend）
```json
{
  "answer": "機器人的回答內容",
  "sources": [
    {
      "source_file": "來源檔案名稱",
      "category": "所屬類別",
      "page_or_section": "第幾頁或哪個段落"
    }
  ],
  "session_id": "對話 session 識別碼"
}
```

---

## 待確認事項
- [ ] API 的 base URL 與 port
- [ ] 是否需要驗證（API Key 或登入）
- [ ] 錯誤回應格式
- [ ] 是否支援串流回應（Streaming）
