# RAG 資料管道說明文件

本文件說明 RAG（Retrieval-Augmented Generation）向量資料庫的資料結構、新增方式與維護方法。

---

## 資料夾結構

```
rag/
├── data/
│   └── raw/
│       ├── websites/        # 爬蟲抓取的官網資料
│       ├── pptx/            # 從 PowerPoint 檔案擷取的內容
│       ├── docx/            # 從 Word 檔案擷取的內容
│       ├── restaurant/      # 餐廳相關資料（手動整理）
│       ├── manual/          # 手動撰寫的補充說明文件
│       └── manual_ppt/      # 手動整理的簡報補充內容
├── src/
│   └── build_vectorstore.py # 向量化主程式
└── vectorstore/             # Chroma 向量資料庫輸出位置（自動產生）
```

---

## 現有資料來源

| 資料夾 | 來源說明 | 備註 |
|--------|----------|------|
| `websites` | 鉅昕鋼鐵官網、旗美農官網爬蟲 | 含產品介紹、公司資訊、聯絡資訊 |
| `pptx` | 公司簡報擷取 | 產品規格、服務說明 |
| `docx` | 公司文件擷取 | 合約範本、說明文件 |
| `restaurant` | 餐廳相關手動整理 | 周邊服務資訊 |
| `manual` | 手動撰寫補充資料 | 常見問題、特殊說明 |
| `manual_ppt` | 手動整理簡報補充 | 額外說明內容 |

---

## JSON 格式規範

每個 JSON 檔案為一個陣列，每筆資料格式如下：

```json
[
  {
    "text": "這裡放要被向量化的文字內容",
    "source_file": "來源檔案名稱（不含副檔名）",
    "source_type": "web / pptx / docx / manual",
    "url": "若為網頁資料填入網址，否則可留空字串",
    "page_or_section": "頁碼或段落說明",
    "category_hint": ["分類標籤1", "分類標籤2"],
    "category": "",
    "date_processed": "YYYY-MM-DD"
  }
]
```

### 欄位說明

| 欄位 | 必填 | 說明 |
|------|------|------|
| `text` | ✅ | 實際內容，是向量化的主體，越清楚越好 |
| `source_file` | ✅ | 來源名稱，用於識別資料從哪裡來 |
| `source_type` | ✅ | 資料類型：`web`、`pptx`、`docx`、`manual` |
| `url` | 否 | 網頁資料填入原始網址 |
| `page_or_section` | 否 | 頁碼或段落，方便追溯來源 |
| `category_hint` | 否 | 分類標籤陣列，輔助理解資料用途 |
| `category` | 否 | 可留空字串 |
| `date_processed` | 否 | 資料處理日期，格式 `YYYY-MM-DD` |

---

## 新增資料的步驟

### 步驟一：準備 JSON 檔案

根據資料類型，在對應資料夾建立新的 `.json` 檔案，遵照上方格式。

> ⚠️ 注意：檔名不可以 `_all_` 開頭，這類檔案會被跳過。

### 步驟二：確認放對資料夾

| 資料類型 | 放入資料夾 |
|----------|------------|
| 官網爬蟲 | `data/raw/websites/` |
| PPT 擷取 | `data/raw/pptx/` |
| Word 擷取 | `data/raw/docx/` |
| 手動撰寫 | `data/raw/manual/` |
| 餐廳資訊 | `data/raw/restaurant/` |

### 步驟三：重新建立向量資料庫

```bash
python src/build_vectorstore.py
```

執行完成後會看到：
```
完成！向量資料庫已儲存至：../vectorstore
共存入 XXX 筆資料
```

> ⚠️ 注意：每次執行都會**刪除舊的向量庫並重建**，請確認所有資料都已備妥再執行。

### 步驟四：更新 backend

將 `rag/vectorstore/` 資料夾整個複製覆蓋到 `backend/rag/vectorstore/`，然後重啟後端服務。

---

## 技術細節

| 項目 | 內容 |
|------|------|
| Embedding 模型 | `paraphrase-multilingual-MiniLM-L12-v2` |
| 向量資料庫 | Chroma（PersistentClient） |
| Collection 名稱 | `rag_collection` |
| 批次大小 | 10 筆 |
| 輸出位置 | `rag/vectorstore/` |

---

## 常見問題

**Q：跑 `build_vectorstore.py` 出現 JSON 解析錯誤怎麼辦？**

先用以下腳本找出壞掉的檔案：

```python
import json, os, glob

RAW_DIRS = ["../data/raw/websites", "../data/raw/pptx", "../data/raw/docx",
            "../data/raw/restaurant", "../data/raw/manual", "../data/raw/manual_ppt"]

for raw_dir in RAW_DIRS:
    for filepath in glob.glob(os.path.join(raw_dir, "*.json")):
        if os.path.basename(filepath).startswith("_all_"):
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ 壞掉的檔案：{filepath}")
            print(f"   錯誤位置：{e}")
```

**Q：Git 合併衝突導致 JSON 壞掉怎麼辦？**

如果檔案裡出現 `<<<<<<< HEAD` 這類標記，用以下腳本修復（保留 HEAD 版本）：

```python
def resolve_conflicts_keep_head(text):
    result = []
    in_head = False
    in_other = False
    for line in text.splitlines(keepends=True):
        if line.startswith("<<<<<<< "):
            in_head = True
            in_other = False
        elif line.startswith("======="):
            in_head = False
            in_other = True
        elif line.startswith(">>>>>>> "):
            in_other = False
        elif in_head or (not in_head and not in_other):
            result.append(line)
    return "".join(result)

with open("壞掉的檔案.json", "r", encoding="utf-8") as f:
    content = f.read()
fixed = resolve_conflicts_keep_head(content)
with open("壞掉的檔案.json", "w", encoding="utf-8") as f:
    f.write(fixed)
```

---

*最後更新：2026-06-03*