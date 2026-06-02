from docx import Document
from datetime import datetime
import os

TEMPLATE_PATH = "template.docx"
OUTPUT_DIR = "output"


def fill_template(data: dict, session_id: str) -> str:
    """將蒐集到的資料填入 Word 範本，儲存為新檔案"""

    # 自動填入建立日期
    data["created_date"] = datetime.now().strftime("%Y/%m/%d")

    # 欄位預設值（避免佔位符殘留在表單上）
    defaults = {
        "name": "", "company": "", "phone": "", "email": "",
        "source": "", "service": "", "quantity_budget": "",
        "spec": "", "date": "", "staff": "", "note": "",
        "created_date": data["created_date"]
    }
    defaults.update(data)
    data = defaults

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = Document(TEMPLATE_PATH)

    # 替換表格中的佔位符
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for key, value in data.items():
                    placeholder = f"{{{{{key}}}}}"
                    if placeholder in cell.text:
                        cell.text = cell.text.replace(placeholder, value or "")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/ticket_{session_id}_{timestamp}.docx"
    doc.save(filename)
    print(f"✅ 已輸出：{filename}")
    return filename