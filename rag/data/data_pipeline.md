# 資料整理流程說明

本文件說明 RAG 向量資料庫的完整資料處理流程，包含各來源的處理方式、手動整理的原因，以及未來更新資料的步驟。

---

## 整體流程概覽

```
原始資料（網站 / PPT / Word / 餐廳 / 手動整理）
        ↓
各來源分別抽取與整理成 JSON
        ↓
build_vectorstore.py 統一向量化
        ↓
Chroma 向量資料庫（vectorstore/）
        ↓
交付給 B 同學的 Backend 模組查詢使用
```

---

## 各來源處理方式

### 1. 網站（crawl_websites.py）

| 項目 | 說明 |
|------|------|
| 來源 | 鉅昕鋼鐵官網、旗美農官網 |
| 工具 | requests + BeautifulSoup |
| 處理方式 | 爬取所有子頁面，去除導覽列、頁首頁尾等雜訊，只保留主要內文 |
| 過濾規則 | 旗美農跳過 productlist、product.aspx、cart、login 等購物頁面 |
| 輸出位置 | `data/raw/websites/` |

### 2. PPT（extract_pptx.py）

| 項目 | 說明 |
|------|------|
| 來源 | 鉅昕集團介紹(完整).pptx、最適合安裝廠房屋頂的不銹鋼鋼瓦太陽能系統.pptx |
| 工具 | python-pptx + EasyOCR |
| 處理方式 | 每張投影片獨立為一筆資料；文字方塊直接抽取，圖片使用 OCR 辨識文字，表格逐列抽取 |
| 限制 | OCR 對模糊圖片或複雜排版辨識效果較差 |
| 輸出位置 | `data/raw/pptx/` |

### 3. Word（extract_docx.py）

| 項目 | 說明 |
|------|------|
| 來源 | 農產品公司介紹.docx、鋼筋加工產業的主要工作.docx、太陽能產業介紹.docx |
| 工具 | python-docx |
| 處理方式 | 讀取所有段落合併成完整文字，因每份文件內容不超過 1000 字，整份當作一筆資料 |
| 限制 | 文件未使用 Word 標題樣式，無法依標題自動分段 |
| 輸出位置 | `data/raw/docx/` |

### 4. 餐廳資料（add_restaurant.py）

| 項目 | 說明 |
|------|------|
| 來源 | 美濃莊餐廳照片描述、菜色說明、菜單、環境介紹 |
| 處理方式 | 由人工根據照片整理成文字描述，直接寫入程式作為結構化資料 |
| 原因 | 餐廳無官方網站可爬取，資料來源為照片，需人工轉換為文字 |
| 輸出位置 | `data/raw/restaurant/` |

### 5. 手動整理 Word（add_manual_docs.py）

| 項目 | 說明 |
|------|------|
| 來源 | 農產品公司介紹、鋼筋加工產業、太陽能產業（三份 Word 的精整版） |
| 處理方式 | 由同學人工閱讀原始文件後，依語意重新切割並整理成高品質段落 |
| 原因 | 程式抽取的 Word 每份只有 1 筆且未分段，語意切割效果差；手動整理可依主題切成多筆，提升搜尋準確度 |
| 輸出位置 | `data/raw/manual/` |

### 6. 手動整理 PPT（add_manual_ppt.py）

| 項目 | 說明 |
|------|------|
| 來源 | 鉅昕集團介紹(完整).pptx 的精整版 |
| 處理方式 | 由同學人工閱讀 PPT 後，依主題整理成結構化段落，補充 OCR 無法辨識的圖片內容 |
| 原因 | PPT 圖片多、流程圖多，OCR 辨識結果雜亂，人工整理後品質顯著提升 |
| 輸出位置 | `data/raw/manual_ppt/` |

---

## 為什麼要同時保留程式抽取與手動整理？

| 來源 | 優點 | 缺點 |
|------|------|------|
| 程式抽取 | 快速、自動化，適合大量資料 | 品質參差不齊，圖片文字辨識有誤差 |
| 手動整理 | 品質高、語意清晰、主題明確 | 耗時，不適合大量資料 |

兩者同時存入向量庫，讓機器人可以從更多角度找到相關資料，互補不足。

---

## 各程式執行順序

如果需要重新建立向量庫，請依以下順序執行：

```bash
# 切換到 extract 資料夾
cd rag/src/extract

# Step 1：爬取網站
python crawl_websites.py

# Step 2：抽取 PPT（含 OCR）
python extract_pptx.py

# Step 3：抽取 Word
python extract_docx.py

# Step 4：新增餐廳資料
python add_restaurant.py

# Step 5：新增手動整理 Word
python add_manual_docs.py

# Step 6：新增手動整理 PPT
python add_manual_ppt.py

# 切換到 src 資料夾
cd ..

# Step 7：重建向量庫
python build_vectorstore.py

# Step 8：測試查詢
python test_query.py
```

---

## 未來更新資料的方式

### 情況一：網站內容更新
重新執行 `crawl_websites.py`，再執行 `build_vectorstore.py` 重建向量庫。

### 情況二：新增 PPT 或 Word 檔案
把新檔案放進對應的 `data/raw/pptx/` 或 `data/raw/docx/` 資料夾，在對應程式的設定區加入新檔案資訊，重新執行該程式，再執行 `build_vectorstore.py`。

### 情況三：新增餐廳菜色或資訊
打開 `add_restaurant.py`，在 `RESTAURANT_DATA` 清單裡新增資料，重新執行，再執行 `build_vectorstore.py`。

### 情況四：B 同學需要更新向量庫
將新的 `vectorstore/` 資料夾整個複製給 B 同學取代舊的，不需要重新安裝任何套件。

---

## 目前向量庫統計

| 來源 | 筆數 |
|------|------|
| 網站（鉅昕鋼鐵） | 42 筆 |
| 網站（旗美農） | 6 筆 |
| PPT（程式抽取） | 79 筆 |
| Word（程式抽取） | 3 筆 |
| 餐廳資料 | 28 筆 |
| 手動整理 Word | 15 筆 |
| 手動整理 PPT | 34 筆 |
| **總計** | **207 筆** |
