"""
手動整理文件新增程式
功能：將Gimini整理的高品質 JSON 資料轉換格式後存入
輸出位置：rag/data/raw/manual/
"""

import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/manual")
TODAY = datetime.now().strftime("%Y-%m-%d")

RAW_DATA = {
    "鋼筋加工產業的主要工作.docx": {
        "category_hint": ["鋼筋加工", "鋼構工程", "鋼材買賣及加工"],
        "docs": [
            {
                "document": "鋼筋加工產業主要作業包含：鋼筋裁切（依尺寸切割長條鋼筋）、彎曲成型（製成梁、柱、箍筋形狀）、鋼筋組立（預先綁紮或焊接成半成品以利施工）、以及客製化加工（依工程需求製作特殊尺寸）。",
                "metadata": {"category": "process", "tags": ["鋼筋加工", "施工流程", "裁切", "彎曲", "鋼筋組立"]}
            },
            {
                "document": "鋼筋加工產業的重要性：鋼筋為混凝土建築之核心結構材料，負擔拉力。其加工精度與品質直接決定了建築安全、結構強度，並影響整體工程進度與施工成本，在公共工程與高樓建築中尤為關鍵。",
                "metadata": {"category": "importance", "tags": ["建築安全", "結構強度", "品質控管"]}
            },
            {
                "document": "鋼筋加工產業特色：屬於傳統製造業，與營建景氣高度連動。近年朝向數位化與自動化轉型，導入自動化裁切彎曲機、ERP生產管理與BIM整合以降低人工誤差；技術面強調看圖能力、機械操作與工程配合。",
                "metadata": {"category": "industry_features", "tags": ["自動化", "BIM", "數位轉型", "製造業"]}
            },
            {
                "document": "鋼筋加工標準作業流程：原料鋼筋進貨 -> 圖面拆料 -> 裁切加工 -> 彎曲成型 -> 品檢分類 -> 出貨至工地 -> 現場綁紮施工。",
                "metadata": {"category": "workflow", "tags": ["標準作業程序", "生產流程", "施工"]}
            },
            {
                "document": "鋼筋加工產業現況與挑戰：產業多以中小企業為主。因面臨嚴重缺工、原料價格波動、工安要求提升及工程規模大型化趨勢，業者正積極發展『自動化加工』與『預組化施工』技術以提升效率。",
                "metadata": {"category": "market_trend", "tags": ["產業挑戰", "缺工", "自動化", "預組化"]}
            },
        ]
    },
    "農產品公司介紹.docx": {
        "category_hint": ["農產品推銷"],
        "docs": [
            {
                "document": "旗美農產業有限公司核心理念為「在地創生＋友善農業＋農產品加工」，長期協助高雄旗山、美濃及台南、屏東地區小農銷售農產品，並致力於提升地方農業價值與推動青年返鄉。",
                "metadata": {"category": "company_profile", "tags": ["旗美農", "在地創生", "友善農業", "小農平台"]}
            },
            {
                "document": "香蕉加工解決滯銷問題：針對旗山香蕉成熟快、保存期短的痛點，旗美農將青香蕉切片、乾燥並研磨成粉，結合傳統關廟麵工法製成「香蕉麵／蕉香麵」系列，有效延長保存期並提升農產品附加價值。",
                "metadata": {"category": "product_innovation", "tags": ["香蕉加工", "青香蕉", "附加價值", "地方創生"]}
            },
            {
                "document": "蕉香麵系列產品特色：主打健康取向，保留青香蕉抗性澱粉，具備低GI、高膳食纖維特性，且無人工色素、無防腐劑，符合現代純素飲食與健康趨勢。",
                "metadata": {"category": "product_features", "tags": ["低GI", "抗性澱粉", "高纖", "健康飲食"]}
            },
            {
                "document": "產品線分類：1. 獨創研發（香蕉麵、蕉香乾拌麵）；2. 健康與加工食品（鳳梨苦瓜雞湯、果乾）；3. 生鮮水果（六龜蓮霧、大內酪梨）；4. 生活選物（面膜、生活用品）。",
                "metadata": {"category": "product_catalog", "tags": ["農產品", "生鮮", "加工食品", "選物"]}
            },
            {
                "document": "企業定位與競爭優勢：旗美農非單純食品電商，而是作為南部農產品整合平台。優勢在於深厚的「地方故事感」、具高差異性的「香蕉麵」文創農產定位，以及結合小農支持與農業品牌化的整合模式。",
                "metadata": {"category": "business_model", "tags": ["地方品牌化", "農業整合", "小農支持", "競爭優勢"]}
            },
        ]
    },
    "太陽能產業介紹.docx": {
        "category_hint": ["太陽能統包設計到送電完成"],
        "docs": [
            {
                "document": "太陽能 EPC 指的是太陽能電廠的統包工程公司，名稱源自 E（Engineering 工程設計）、P（Procurement 採購）、C（Construction 施工建置），負責將太陽能電廠從土地評估到正式併聯發電的完整過程。",
                "metadata": {"category": "definition", "tags": ["EPC", "太陽能", "定義"]}
            },
            {
                "document": "EPC 主要工作內容包含：一、工程設計（系統容量規劃、鋼構支架設計、台電/能源局法規申請）；二、材料採購（太陽能模組、逆變器、鋼構支架如C型鋼/H型鋼、配電設備）；三、施工建置（基樁工程、鋼構組立、模組安裝、測試與試運轉）。",
                "metadata": {"category": "main_tasks", "tags": ["工程設計", "採購", "施工", "太陽能模組"]}
            },
            {
                "document": "太陽能 EPC 的獲利模式主要包含整體工程毛利、透過大量採購產生的材料價差、透過設計最佳化節省成本，以及電廠完工後的長期維運（O&M）收入。",
                "metadata": {"category": "business_model", "tags": ["工程利潤", "維運", "成本控制"]}
            },
            {
                "document": "EPC 產業的核心競爭能力包括：專案管理能力（整合土建、鋼構、電機與台電協調）、成本控制能力（應對材料價格波動）、現場施工品質（影響發電效率與安全）以及對政府法規流程的熟悉度。",
                "metadata": {"category": "core_competencies", "tags": ["專案管理", "成本控制", "法規"]}
            },
            {
                "document": "EPC 產業的風險與未來趨勢：面臨原物料價格波動與工期延誤等風險。未來趨勢朝向大型化、儲能整合、高壓電工程、AI監控維運與綠電交易發展，具備資金調度與長期維運能力的廠商更具競爭力。",
                "metadata": {"category": "trends_risks", "tags": ["原物料波動", "儲能", "綠電", "未來趨勢"]}
            },
        ]
    },
}


def convert_and_save():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = []

    for source_file, content in RAW_DATA.items():
        results = []
        category_hint = content["category_hint"]

        for i, item in enumerate(content["docs"]):
            results.append({
                "text": item["document"],
                "source_file": source_file,
                "source_type": "manual",
                "page_or_section": item["metadata"].get("category", f"段落{i+1}"),
                "category_hint": category_hint,
                "category": "",
                "tags": item["metadata"].get("tags", []),
                "date_processed": TODAY
            })

        out_name = source_file.replace(".docx", "_manual.json")
        out_path = os.path.join(OUTPUT_DIR, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        print(f"完成：{source_file} → {len(results)} 筆")
        all_results.extend(results)

    merged_path = os.path.join(OUTPUT_DIR, "_all_manual.json")
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\n全部完成！共 {len(all_results)} 筆手動整理資料")


if __name__ == "__main__":
    convert_and_save()