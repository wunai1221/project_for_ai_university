# project_for_ai_university

## 專案簡介
本專案為一個結合 RAG（Retrieval-Augmented Generation）技術的問答機器人網站，
針對鉅昕集團旗下六大業務（鋼筋加工、鋼構工程、鋼材買賣及加工、
太陽能統包、餐廳推廣、農產品推銷）提供智慧問答服務，
能夠根據多種來源的知識庫（網站、簡報、Word 文件）回答使用者問題。

---

## 團隊分工

| 成員 | 負責模組 | 資料夾 |
|------|----------|--------|
| A 同學 | 前端網站介面 | `/frontend` |
| B 同學 | 後端主程式 & 機器人邏輯 | `/backend` |
| 我     | 資料處理 & RAG 向量資料庫 | `/rag` |

---

## 專案資料夾結構

```
rag-chatbot-project/
│
├── frontend/          # A 同學負責：網站前端
├── backend/           # B 同學負責：主程式與機器人
├── rag/               # 我負責：資料處理與向量資料庫
├── shared/            # 三人共用的設定、格式規範
├── docs/              # 文件、會議記錄、交付說明
└── README.md          # 本文件
```

---

## 各模組說明

### Frontend（A 同學）
請見 `/frontend/README.md`

### Backend（B 同學）
請見 `/backend/README.md`

### RAG 資料庫（我）
請見 `/rag/README.md`

---

## 模組之間的串接方式

```
使用者輸入問題
     ↓
Frontend 傳送問題給 Backend API
     ↓
Backend 呼叫 RAG 向量資料庫查詢相關段落
     ↓
Backend 將查詢結果 + 問題組合後送給 LLM
     ↓
LLM 生成回答，回傳給 Frontend 顯示
```

### 重要介面約定（三人需對齊）
- Frontend ↔ Backend：API 格式請見 `/shared/api_spec.md`
- Backend ↔ RAG：向量庫查詢方式請見 `/shared/vectorstore_spec.md`

---

## 環境需求
- Python 3.10+
- Node.js（前端，版本由 A 同學確認）
- 詳細套件請見各子模組的 `requirements.txt` 或 `package.json`

# 鉅昕鋼鐵前端開啟方式

---

# 一、安裝 Node.js

在執行前端專案前，請先安裝 Node.js。

## 官方下載網址

```txt
https://nodejs.org/
```

建議安裝：

```txt
LTS（Long Term Support）版本
```

---

# 二、確認 Node.js 安裝成功

打開 VS Code Terminal 或 PowerShell，輸入：

```bash
node -v
npm -v
```

---

# 三、使用 VS Code 開啟專案

請確認開啟的是：

```txt
專案最外層根目錄
```

也就是有：

```txt
package.json
tsconfig.json
```

的那一層資料夾。

---

# 四、開啟 VS Code Terminal

上方選單：

```txt
Terminal
→
New Terminal
```

---

# 五、安裝前端套件

在 Terminal 輸入：

```bash
npm install
```

或：

```bash
npm i
```

安裝完成後會出現：

```txt
node_modules/
```

資料夾。

---

# 六、啟動前端開發伺服器

輸入：

```bash
npm run dev
```

如果專案使用 Bun：

```bash
bun dev
```

---

# 七、開啟瀏覽器

Terminal 會出現：

```txt
Local: http://localhost:8080/
```

或：

```txt
Local: http://localhost:5173/
```

直接：

- Ctrl + 點擊網址
- 或手動貼到瀏覽器

即可開啟網站。

---
