# RAG 資料處理模組

## 負責範圍
本資料夾負責將所有原始資料（網站、簡報、Word、餐廳資料）處理成可被查詢的向量資料庫，
供 B 同學的 Backend 模組使用。

---

## 核心設計原則

> **以「內容段落」為單位，而非「檔案」為單位**
>
> 同一份簡報可能包含多個主題，因此每張投影片、每個段落都會被獨立處理與分類，
> 讓機器人能夠跨檔案、跨格式找到最相關的內容，
> 不會因為資訊藏在某份簡報的某一頁就找不到。

---

## 原始資料來源

| 類型 | 數量 | 存放位置 |
|------|------|----------|
| 網站 | 2 個 | `/rag/data/raw/websites/` |
| 簡報（PPTX） | 2 份 | `/rag/data/raw/pptx/` |
| Word（DOCX） | 3 份 | `/rag/data/raw/docx/` |
| 餐廳資料 | 28 筆 | `/rag/data/raw/restaurant/` |
| 手動整理 Word | 3 份 | `/rag/data/raw/manual/` |
| 手動整理 PPT | 1 份 | `/rag/data/raw/manual_ppt/` |

---

## 六大知識類別

1. 鋼筋加工
2. 鋼構工程
3. 鋼材買賣及加工
4. 太陽能統包設計到送電完成
5. 餐廳推廣
6. 農產品推銷

---

## 各原始資料與類別對應

| 檔案名稱 | 類別 |
|---------|------|
| 鉅昕鋼鐵官網 | 鋼筋加工、鋼構工程、鋼材買賣及加工 |
| 旗美農官網 | 農產品推銷 |
| 農產品公司介紹.docx | 農產品推銷 |
| 鋼筋加工產業的主要工作.docx | 鋼筋加工、鋼構工程、鋼材買賣及加工 |
| 太陽能產業介紹.docx | 太陽能統包設計到送電完成 |
| 鉅昕集團介紹(完整).pptx | 六大類別皆有 |
| 最適合安裝廠房屋頂的不銹鋼鋼瓦太陽能系統.pptx | 太陽能統包設計到送電完成 |
| restaurant_data.json | 餐廳推廣 |
| 鉅昕集團介紹(完整).pptx（手動整理版） | 鋼筋加工、鋼構工程、鋼材買賣及加工、太陽能統包設計到送電完成、農產品推銷 |
| 農產品公司介紹.docx（手動整理版） | 農產品推銷 |
| 鋼筋加工產業的主要工作.docx（手動整理版） | 鋼筋加工、鋼構工程、鋼材買賣及加工 |
| 太陽能產業介紹.docx（手動整理版） | 太陽能統包設計到送電完成 |

---

## 處理流程

```
原始資料（網站/PPTX/DOCX/餐廳/手動整理）
        ↓
  Step 1：抽取文字
  網站       → crawl_websites.py（含雜訊過濾）
  PPTX      → extract_pptx.py（含 EasyOCR 圖片文字辨識）
  DOCX      → extract_docx.py
  餐廳資料   → add_restaurant.py（菜色、環境、菜單描述）
  手動整理Word → add_manual_docs.py
  手動整理PPT  → add_manual_ppt.py
        ↓
  Step 2：向量化並存入資料庫
  build_vectorstore.py
  （使用 paraphrase-multilingual-MiniLM-L12-v2 模型）
        ↓
  輸出：vectorstore/ 資料夾（交付給 B 同學）
```

---

## 資料夾結構

```
rag/
├── README.md
├── requirements.txt
│
├── data/
│   └── raw/
│       ├── websites/     # 網站爬取結果（JSON）
│       ├── pptx/         # PPT 抽取結果（JSON）
│       ├── docx/         # Word 抽取結果（JSON）
│       ├── restaurant/   # 餐廳菜色與環境描述（JSON）
│       ├── manual/       # 手動整理 Word（JSON）
│       └── manual_ppt/   # 手動整理 PPT（JSON）
│
├── src/
│   ├── extract/
│   │   ├── crawl_websites.py    # 網站爬蟲
│   │   ├── extract_pptx.py      # PPT 抽取（含OCR）
│   │   ├── extract_docx.py      # Word 抽取
│   │   ├── add_restaurant.py    # 餐廳資料新增
│   │   ├── add_manual_docs.py   # 手動整理 Word 新增
│   │   └── add_manual_ppt.py    # 手動整理 PPT 新增
│   ├── build_vectorstore.py     # 向量化與建立資料庫
│   └── test_query.py            # 查詢測試
│
└── vectorstore/          # 最終向量資料庫（交付給 B 同學）
```

---

## 每筆資料的格式

```json
{
  "text": "段落內文",
  "source_file": "來源檔案名稱",
  "source_type": "web / pptx / docx / restaurant / manual / manual_ppt",
  "page_or_section": "第3張投影片 / 網址 / 開頭 / 招牌菜色",
  "category_hint": ["鋼筋加工"],
  "category": "餐廳推廣",
  "date_processed": "2026-06-01"
}
```

---

## 向量資料庫資訊

| 項目 | 說明 |
|------|------|
| 向量庫格式 | Chroma |
| 資料夾位置 | `/rag/vectorstore/` |
| Embedding 模型 | paraphrase-multilingual-MiniLM-L12-v2 |
| 總筆數 | 207 筆 |
| 查詢回傳筆數 | top-5 |

---

## 環境設定

### 安裝套件
```bash
pip install chromadb sentence-transformers python-pptx python-docx beautifulsoup4 requests easyocr Pillow numpy
```

### B 同學只需要安裝
```bash
pip install chromadb sentence-transformers
```
第一次執行會自動下載 Embedding 模型，需要網路連線。

---

## 交付給 B 同學的東西

1. `/rag/vectorstore/` 資料夾
2. `/shared/vectorstore_spec.md`
3. `/rag/src/test_query.py` 查詢範例

**B 同學注意：查詢時必須使用相同的 Embedding 模型 `paraphrase-multilingual-MiniLM-L12-v2`**
