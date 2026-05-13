"""
Word 文件抽取程式
功能：讀取 DOCX 檔案，依段落切割，儲存成 JSON 格式
輸出位置：rag/data/raw/docx/
"""

import json
import os
from datetime import datetime
from docx import Document

# ============================================================
# 設定區
# ============================================================
DOCX_FILES = [
    {
        "filename": "農產品公司介紹.docx",
        "category_hint": ["農產品推銷"]
    },
    {
        "filename": "鋼筋加工產業的主要工作.docx",
        "category_hint": ["鋼筋加工", "鋼構工程", "鋼材買賣及加工"]
    },
    {
        "filename": "太陽能產業介紹.docx",
        "category_hint": ["太陽能統包設計到送電完成"]
    },
]

# 原始檔案放置位置（你的 docx 檔案放這裡）
INPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/docx")

# 輸出位置
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/docx")

# 段落最少字數（太短的段落跳過，避免雜訊）
MIN_CHARS = 20
# ============================================================


def extract_docx(filepath: str, file_info: dict) -> list[dict]:
    """讀取 DOCX，依段落切割成多筆資料"""
    doc = Document(filepath)
    filename = file_info["filename"]
    category_hint = file_info["category_hint"]

    results = []
    current_section = ""
    current_heading = "開頭"

    for para in doc.paragraphs:
        text = para.text.strip()

        if not text:
            continue

        # 如果是標題，記錄起來當作 metadata
        if para.style.name.startswith("Heading"):
            # 先儲存上一個段落
            if len(current_section) >= MIN_CHARS:
                results.append({
                    "text": current_section.strip(),
                    "source_file": filename,
                    "source_type": "docx",
                    "page_or_section": current_heading,
                    "category_hint": category_hint,
                    "category": "",
                    "date_processed": datetime.now().strftime("%Y-%m-%d")
                })
            # 開始新段落
            current_heading = text
            current_section = ""
        else:
            current_section += text + "\n"

    # 儲存最後一個段落
    if len(current_section) >= MIN_CHARS:
        results.append({
            "text": current_section.strip(),
            "source_file": filename,
            "source_type": "docx",
            "page_or_section": current_heading,
            "category_hint": category_hint,
            "category": "",
            "date_processed": datetime.now().strftime("%Y-%m-%d")
        })

    return results


def main():
    all_results = []

    for file_info in DOCX_FILES:
        filepath = os.path.join(INPUT_DIR, file_info["filename"])

        if not os.path.exists(filepath):
            print(f"找不到檔案：{filepath}，請確認檔案是否放在 data/raw/docx/ 資料夾")
            continue

        print(f"處理：{file_info['filename']}")
        results = extract_docx(filepath, file_info)
        print(f"  → 切出 {len(results)} 個段落")

        # 各自儲存
        out_name = file_info["filename"].replace(".docx", ".json")
        out_path = os.path.join(OUTPUT_DIR, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        all_results.extend(results)

    # 合併儲存
    merged_path = os.path.join(OUTPUT_DIR, "_all_docx.json")
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\n完成！共切出 {len(all_results)} 個段落")
    print(f"合併檔案：{merged_path}")


if __name__ == "__main__":
    main()