# 環境設定說明

> 本文件由三位組員共同維護，請各自把自己負責模組需要的環境設定補充進來。

---

## 共同需求

- Python 3.10+
- Node.js（版本由 A 同學確認後填入）
- Git

---

## RAG 模組（我負責）

### 需要安裝的套件
```bash
pip install chromadb sentence-transformers python-pptx python-docx beautifulsoup4 requests easyocr Pillow numpy
```

### 會自動下載的模型（需要網路，只有第一次）
- Embedding 模型：`paraphrase-multilingual-MiniLM-L12-v2`
- EasyOCR 中文辨識模型

### B 同學查詢向量庫只需要安裝
```bash
pip install chromadb sentence-transformers
```
第一次執行會自動下載 Embedding 模型，之後不用重複下載。

查詢範例請參考 `rag/src/test_query.py`

---

## Backend 模組（B 同學負責）

> B 同學請把你需要的套件和環境設定補充在這裡

### 需要安裝的套件
```bash
# 待補充
```

### 其他設定
- 待補充

---

## Frontend 模組（A 同學負責）

> A 同學請把你需要的套件和環境設定補充在這裡

### 需要安裝的套件
```bash
# 待補充
```

### Node.js 版本
- 待補充

### 其他設定
- 待補充

---

## 統整：目前已確認需要安裝的東西

> 隨著大家補充，這裡會越來越完整

| 套件／工具 | 用途 | 誰需要 |
|-----------|------|--------|
| Python 3.10+ | 執行程式 | 全部 |
| chromadb | 向量資料庫 | RAG、Backend |
| sentence-transformers | Embedding 模型 | RAG、Backend |
| easyocr | PPT 圖片文字辨識 | RAG |
| python-pptx | 讀取 PPT | RAG |
| python-docx | 讀取 Word | RAG |
| beautifulsoup4 | 網站爬蟲 | RAG |
| requests | 網路請求 | RAG |
| Pillow | 圖片處理 | RAG |
| numpy | 數值計算 | RAG |
| 待補充 | 待補充 | Backend |
| 待補充 | 待補充 | Frontend |
