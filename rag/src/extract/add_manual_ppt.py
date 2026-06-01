"""
PPT 手動整理資料新增程式
功能：將Gmini整理的 PPT 高品質內容轉換格式後存入
輸出位置：rag/data/raw/manual_ppt/
"""

import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/manual_ppt")
TODAY = datetime.now().strftime("%Y-%m-%d")

MANUAL_PPT_DATA = [
    {"document": "鉅昕鋼鐵擁有多項專利，包括『增強型鋼架』(2023, 台灣)、『快搭式樑柱成型組合鋼構』(2022, 台灣)、『可回收的焊接用背襯』(2022, 台灣) 以及多項日本與中國專利（如：アンカーボルト、基礎螺栓、定位調整器等）。", "metadata": {"category": "patents", "tags": ["專利", "研發", "知識產權"]}},
    {"document": "核心技術：JC抗震基礎螺栓。該技術將牙棒部位加粗與鋼筋一體磨擦壓接成型，比傳統基礎螺栓更具抗拉力，並可使用鋼筋廢料製作，符合節能減碳要求。", "metadata": {"category": "core_technology", "tags": ["JC抗震基礎螺栓", "抗震", "節能減碳"]}},
    {"document": "抗震效能驗證：科技部專案研究與高雄科技大學合作證實，鉅昕抗震基礎螺栓的強度與抗震效能皆優於傳統螺栓組，具備更好的力學表現。", "metadata": {"category": "verification", "tags": ["科技部專案", "抗震效能", "力學實驗"]}},
    {"document": "施工效率優勢：透過抗震基礎鋼筋座與免拆模板技術，單柱體施工工時可從傳統工法的 40 工時大幅縮減至 6 工時，節省工時達 85%。", "metadata": {"category": "efficiency", "tags": ["節省工時", "施工效率", "預組化施工"]}},
    {"document": "核心技術應用：包含抗震基礎鋼筋座（一體成型、提升抗震傳導力）、免拆模板（於廠內預先焊接於基礎座上以節省工地時間）及3D立體精密定位技術。", "metadata": {"category": "technical_details", "tags": ["抗震基礎鋼筋座", "免拆模板", "3D定位"]}},
    {"document": "現場施工技術：提供「地樑精準接合」與「免拆模板預焊安裝」技術。在地樑接合處採用精準鋼筋接合，並於廠內預先將免拆模板焊接安裝，大幅降低工地現場施工難度與時間。", "metadata": {"category": "site_construction", "tags": ["地樑接合", "免拆模板", "現場施工", "預組化"]}},
    {"document": "專利精密定位技術：運用專利設計的鋼構模具與定位系統，實現3D立體精密定位，確保鋼筋組立的高準確度與快速安裝能力。", "metadata": {"category": "precision_technology", "tags": ["3D定位", "精密定位", "專利技術"]}},
    {"document": "施工效益驗證：經實驗證實，鋼筋鋼構化（採用焊接與續接器）之耐震度與抗震效能均優於傳統鐵絲綁紮，且能節省工地工時達 85%（從 40 工時縮減至 6 工時），具備顯著的效率與安全優勢。", "metadata": {"category": "efficiency_verification", "tags": ["抗震", "施工效率", "工時節省", "耐震度"]}},
    {"document": "預鑄桁架樓承板：廠內量產之預鑄桁架樓承板，透過自動化設備生產，結構均勻且規格統一，優化結構施工品質。", "metadata": {"category": "precast_products", "tags": ["樓承板", "預鑄", "自動化生產"]}},
    {"document": "和發廠區營運實拍：和發廠區具備現代化寬敞空間，配置大型橋式起重機，廠內設有專屬鋼筋預組化生產線，展現工業 4.0 規格之自動化營運能力。", "metadata": {"category": "factory_operations", "tags": ["和發廠", "工業4.0", "廠房設施", "自動化產線"]}},
    {"document": "專利續接器製造：家興鋼鐵專注於鋼筋續接器生產，擁有多項專利，包括防鏽鋼筋續接器處理方法、鋼筋續接器與鋼筋之螺接構造、鋼筋錨錠接頭及防鬆脫型鋼筋續接器等。", "metadata": {"category": "patents_production", "tags": ["續接器", "專利", "鋼筋連接", "防鏽"]}},
    {"document": "專利複合螺紋無接縫快速續接器：採用導引設計，可徒手鎖入，接合後無扭力值問題，強度增強達 150%，不需額外工具即可達 SA 級檢測標準，市佔率達 100%，年銷售超過 30 萬組。", "metadata": {"category": "product_features", "tags": ["快速續接器", "市佔率", "抗震", "施工效率"]}},
    {"document": "鋼構與太陽光電工程：承錡鋼鐵提供鋼構與太陽光電工程的設計與統包服務，具備大型吊裝與鋼構建築施工能力。", "metadata": {"category": "construction_services", "tags": ["鋼構", "太陽能EPC", "統包", "工程設計"]}},
    {"document": "和發廠房設計：主結構採用角槽鋼模組化鎖固設計取代傳統 H 型鋼，大量節省鋼材重量，達到減碳與降低成本之目標。基礎採用抗震預組焊鋼筋基礎座，符合綠能減碳需求。", "metadata": {"category": "facility_design", "tags": ["角槽鋼", "模組化", "綠能減碳", "鋼構設計"]}},
    {"document": "營建工程實績：耀旺營造負責各類營建工程，包括地樑精準接合、免拆模板預焊安裝及各類鋼筋基礎工程，展現精準施工與模組化安裝能力。", "metadata": {"category": "construction_projects", "tags": ["營造工程", "地樑", "預焊安裝", "施工"]}},
    {"document": "工業設備製造：嘉佑工業專精於設備與鍋爐工程製造，提供重工業級的工程解決方案。", "metadata": {"category": "industrial_manufacturing", "tags": ["鍋爐", "設備製造", "重工業"]}},
    {"document": "企業社會責任 (CSR-ESG)：日高綠能科技推廣創新建材「鋼瓦型太陽能屋頂板」，結合屋頂與太陽能模組，具備自潔、重量輕、易安裝、不滲水、省支架與設計美觀六大特色。", "metadata": {"category": "csr_esg", "tags": ["ESG", "太陽能屋頂", "創新建材", "綠色能源"]}},
    {"document": "鋼瓦型太陽能系統：採用雙層鋼板設計，具備防水與隔熱功能。相較於一般玻璃型太陽能板，鋼瓦型設計能與屋頂建築結合為一、無間隙，且具備重量輕、施工堅固、維護容易及防火防漏水等優勢。", "metadata": {"category": "solar_technology", "tags": ["鋼瓦型太陽能", "屋頂翻新", "防水隔熱", "建築整合"]}},
    {"document": "循環農業系統：導入免動力揚水機與「魚蝦菇菜共生」系統。透過綠能雙循環水力發電系統，結合全環控蔬菜栽培、菇類栽培與水產養殖，達成資源高效循環利用。", "metadata": {"category": "circular_agriculture", "tags": ["循環農業", "魚菜共生", "免動力揚水機", "綠能發電"]}},
    {"document": "農業廢棄物循環再利用：旗美農產業有限公司開發「農業廢棄物多元應用處理設備」，並取得中華民國新型專利 (專利證書第 M606814 號，期間至 2030 年)，旨在提升農業資源利用率。", "metadata": {"category": "environmental_patents", "tags": ["農業廢棄物", "專利", "循環經濟", "環保"]}},
    {"document": "友善農業推廣：羅依國際股份有限公司致力於推動無毒有機耕作，開發無毒有機除草劑，並透過舉辦在地農業活動，促進綠色生活與環境友善耕作。", "metadata": {"category": "organic_farming", "tags": ["無毒農業", "有機除草劑", "友善耕作", "企業責任"]}},
    {"document": "旗美農產業有限公司的企業社會責任 (CSR) 重點在於解決在地農業問題：推動地方創生、建立滯農銀行、開發在地農產品。針對國內香蕉滯銷問題，透過加工技術提升附加價值。", "metadata": {"category": "csr_initiatives", "tags": ["CSR", "在地創生", "滯農問題", "農業品牌化"]}},
    {"document": "太陽能安裝工法與流程：標準施工程序包含：1. 進料吊掛、2. 支架鋪設、3. 模組鋪設、4. 收邊包覆、5. 棧道組裝、6. 線路組裝。此流程確保太陽能發電系統與廠房屋頂完整整合，提升耐用度與美觀。", "metadata": {"category": "installation_workflow", "tags": ["安裝流程", "施工方式", "太陽能屋頂"]}},
    {"document": "不鏽鋼屋瓦太陽能優勢：保護廠房屋頂不漏水、將鋼瓦壽命延長三倍、提升抗颱風能力。與一般玻璃型太陽能板相比，具備無間隙安裝、輕量化、抗風壓 (7000psi)、抗腐蝕及易清洗等顯著優勢。", "metadata": {"category": "product_advantages", "tags": ["不鏽鋼屋瓦", "抗颱風", "屋頂翻新", "模組強度"]}},
    {"document": "傳統太陽能發電模組結構問題：面對風災威脅，常見結構隱憂包含結構設計不足、支架生鏽或鬆脫、模組受風面積過大，以及地震隱患。統計指出台灣一年平均面臨3.5個颱風，傳統架設方式需承擔高額的20年維運風險。", "metadata": {"category": "structural_risk", "tags": ["風災", "結構安全", "維運風險", "颱風"]}},
    {"document": "太陽能火災風險分析：根據英國建築研究院 (BRE) 調查，太陽能意外原因分析如下：安裝不當佔36%、維運問題佔47%、產品故障佔12%、設計錯誤佔5%。日本十年內亦發生超過127起因缺乏定期檢查而引發的火災事故。", "metadata": {"category": "fire_risk", "tags": ["火災", "安裝不當", "維運", "事故分析"]}},
    {"document": "傳統太陽能發電模組的漏水風險：安裝於鋼板或石棉瓦屋頂時，若未更換老舊屋頂，容易因結構老化導致破損漏水。此外，太陽能板長期重壓易使屋頂變形，或因熱脹冷縮導致接縫處矽利康硬化裂開，進而造成漏水問題。", "metadata": {"category": "water_leakage_risk", "tags": ["漏水", "屋頂結構", "矽利康", "變形"]}},
    {"document": "太陽能模組清洗與維運挑戰：太陽能板需定期清洗（建議平均半年一次，視環境而定），方式包含高壓沖洗配合人工刷洗或專用清洗機。清洗的必要性在於落塵與髒污會嚴重影響發電效率。", "metadata": {"category": "maintenance", "tags": ["清洗", "發電效率", "維運"]}},
    {"document": "輕量型金屬太陽能鋼板與一般玻璃型模組比較：輕量型鋼板採用 ETFE 薄膜，具備高透光 (96%以上) 與自潔功能，重量輕 (7.07Kg/m2)，抗風壓高達 7000psi。安裝方式如同安裝浪板，可與屋頂結合無間隙，防水性優，防火與結構堅固度亦優於傳統玻璃型模組。", "metadata": {"category": "product_comparison", "tags": ["輕量型鋼板", "玻璃模組", "抗風壓", "防水"]}},
    {"document": "工研院發電量測結果：於相同裝機容量 (4.8kW) 下，實測期間統計顯示，「鋼板單晶」總發電度數 (165.33 kWh) 優於「玻璃單晶」(154.97 kWh)。在每單位容量平均每日發電度數上，鋼板單晶 (3.44 kWh/kW) 亦高於玻璃單晶 (3.23 kWh/kW)。", "metadata": {"category": "performance_verification", "tags": ["工研院", "發電效率", "實測數據", "效能比較"]}},
    {"document": "產品認證與安全性：輕量型太陽能模組已通過國家標準自願性產品驗證 (VPC)，使用通過認證之高效模組者可額外加成 6% 躉購費率。此外，該產品已取得 IEC61215、IEC61730 及 UL1703 等多項國際測試報告驗證。", "metadata": {"category": "certifications", "tags": ["VPC", "IEC61215", "UL1703", "躉購費率", "產品驗證"]}},
    {"document": "太陽能模組維護計畫：建議維護頻率包含每日發電數據監控、即時系統異常通知、48小時內故障排除，以及每三個月執行一次模組清洗與電廠巡檢維護。", "metadata": {"category": "maintenance_plan", "tags": ["維運", "監控", "清潔", "故障排除"]}},
    {"document": "智慧監控系統：系統具備24小時雲端監控，可即時查看日射量、光電溫度，並自動產出資料分析報表，透過即時資料監控，能有效提升電廠整體發電效率與故障診斷準確率。", "metadata": {"category": "smart_monitoring", "tags": ["雲端監控", "數據分析", "智慧電廠"]}},
    {"document": "集團關聯企業包含：承錡鋼鐵、羅依國際、嘉佑工業、旗美農產業、鉅昕鋼鐵、日高綠能科技、耀旺營造、御揚國際、家興鋼鐵。", "metadata": {"category": "group_structure", "tags": ["集團架構", "子公司"]}},
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = []
    for i, item in enumerate(MANUAL_PPT_DATA):
        results.append({
            "text": item["document"],
            "source_file": "鉅昕集團介紹(完整).pptx",
            "source_type": "manual_ppt",
            "page_or_section": item["metadata"].get("category", f"段落{i+1}"),
            "category_hint": ["鋼筋加工", "鋼構工程", "鋼材買賣及加工",
                              "太陽能統包設計到送電完成", "農產品推銷"],
            "category": "",
            "tags": item["metadata"].get("tags", []),
            "date_processed": TODAY
        })

    out_path = os.path.join(OUTPUT_DIR, "manual_ppt_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(results)} 筆 PPT 手動整理資料")
    print(f"儲存至：{out_path}")


if __name__ == "__main__":
    main()