# Backend 後端模組（B 同學負責）

## 負責範圍
本資料夾為網站的後端主程式，包含機器人邏輯與 API 伺服器。

## 主要功能（預計）
- 提供 API 給前端呼叫（接收問題、回傳答案）
- 呼叫 RAG 向量資料庫，取得與問題最相關的知識段落
- 將查詢結果組合成 Prompt，送給 LLM 生成最終回答
- 管理對話歷史（若有多輪對話需求）

## 與其他模組的串接

### 和 Frontend（A 同學）
- 提供 REST API，格式請見 `/shared/api_spec.md`

### 和 RAG 資料庫（我）
- 載入我交付的向量資料庫（Chroma 格式，一個資料夾）
- 使用的 Embedding 模型請對齊 `/shared/vectorstore_spec.md` 的說明
- 查詢方式為：輸入使用者問題 → 回傳最相關的 top-k 段落

## 資料夾結構（B 同學自行規劃）
```
backend/
├── README.md       # 本文件
├── main.py         # 主程式入口
└── ...
```

## 注意事項
- **Embedding 模型必須與 RAG 端使用同一個**，否則查詢結果會錯誤
- 向量庫載入與查詢範例請見 `/shared/vectorstore_spec.md`
- 如需調整分類或新增知識來源，請通知我重新處理
