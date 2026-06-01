"""
餐廳資料新增程式
功能：將餐廳的菜色、環境、菜單描述加入向量資料庫
"""

import json
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/restaurant")

TODAY = datetime.now().strftime("%Y-%m-%d")

RESTAURANT_DATA = [
    # ========== 菜單 ==========
    {
        "text": "美濃莊年菜菜單。伍仟捌百元套餐包含：五福臨門祥臻拼盤、八寶呈瑞海鮮羹、潤玉珍選虎斑、金蒜獻瑞粉蒸白蝦、櫻花映福嚴選米糕、筍香納福封肉、祥瑞滿堂佛跳牆、養生納福烏骨藥膳湯、五彩如意時蔬、瑞彩堂果。捌千捌百元套餐包含：五福臻選拼盤、玉月酥蝦餅、八寶呈瑞海羹、瑞彩堂果、玉潤極鮮虎斑、蒜香臻品九孔、金煎明蝦、金酥御鴨、筍香納福封肉、祥瑞滿堂佛跳、御膳烏骨藥饌、干貝呈瑞櫻花、五彩如意時蔬。",
        "source_file": "美濃莊年菜菜單",
        "source_type": "restaurant",
        "page_or_section": "年菜菜單",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 環境介紹 ==========
    {
        "text": "美濃莊餐廳擁有超大型開放式宴會廳，天花板上掛滿數十個吊扇和方形平板燈，整個空間擺滿了數十張圓桌，每一張都坐滿了人，氛圍非常熱絡，適合大型鄉鎮活動、喜宴、尾牙。另有現代風大型圓桌宴會廳，配有透明轉盤，圍繞著十多張灰背橘墊現代椅，背景是白色磚牆和大型窗戶，採光良好，適合大型公司聚餐、團體活動、會議。",
        "source_file": "美濃莊環境介紹",
        "source_type": "restaurant",
        "page_or_section": "大型宴會廳",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "美濃莊餐廳備有較小型的包廂空間，配有木紋牆、深咖啡色皮椅與圓形轉盤餐桌，空間安靜隱密，適用於小組會議、私人聚餐。餐廳也提供設有大型電子白板的會議型餐廳空間，適合公司會議餐、尾牙、慶功宴。另有多人大型轉盤圓桌，適合15人以上聚餐，適合團隊建設、春酒、慶功宴。",
        "source_file": "美濃莊環境介紹",
        "source_type": "restaurant",
        "page_or_section": "包廂與會議空間",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 地理位置 ==========
    {
        "text": "美濃莊餐廳位於馬路邊，擁有寬敞的店前停車空間，門口設有明顯的紅底白字招牌，建築外觀開闊，交通便利，適合自駕顧客。餐廳平日與假日生意皆相當興隆，經常呈現座無虛席的狀態，建議提前訂位。",
        "source_file": "美濃莊地理位置",
        "source_type": "restaurant",
        "page_or_section": "地理位置與交通",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 菜色第一批 ==========
    {
        "text": "蔥油土雞：白斬雞切塊鋪底，上方鋪滿細蔥絲與紅辣椒絲，淋上蔥油，色澤鮮亮誘人，口感清爽且蔥香濃郁，是經典的冷盤菜。適合宴客。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-蔥油土雞",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "梅干扣肉：肥瘦相間的五花肉整齊排列，燉煮至深褐色，吸收了濃郁的梅干菜香氣與鹹甜醬汁，肉質軟嫩入味，非常下飯，是客家傳統美食。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-梅干扣肉",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "涼拌捲餅／水晶捲：透明外皮包裹著紅蘿蔔絲、小黃瓜絲與酥脆食材，切片擺盤，外觀層次分明，口感爽脆，具有清爽感，適合開胃。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-涼拌捲餅",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "炒粄條：經典客家炒粄條，加入韭菜、豆芽菜與肉絲大火快炒，粄條呈半透明且吸附了醬油香氣，鑊氣十足，是客家主食代表。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-炒粄條",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "蛤蜊雞湯／藥膳雞湯：深色的濃郁湯頭，內含雞肉塊、蛤蜊與藥膳食材（紅棗、枸杞等），湯面油光飽滿，視覺上顯得滋補且鮮甜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-藥膳雞湯",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "蘿蔔排骨湯：清澈的湯頭搭配塊狀蘿蔔與排骨，色澤透亮，口感鮮甜純淨，適合搭配重口味菜色，是經典家常湯品。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-蘿蔔排骨湯",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "鳳梨蝦球：炸得金黃的蝦球淋上美乃滋，周圍擺放鳳梨切片與橘子果瓣點綴，色彩鮮豔且充滿水果酸甜香氣，非常受歡迎的人氣料理。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-鳳梨蝦球",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "涼拌豆干絲：細長的豆干絲、紅蘿蔔絲與韭菜段涼拌，色澤深邃帶有醬汁感，口感爽脆，是常見的風味開胃小菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-涼拌豆干絲",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "炒筍絲大腸：筍絲與處理乾淨的大腸快炒，佐以辣椒絲，口感脆嫩且酸香入味，是道地的客家熱炒風味。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-炒筍絲大腸",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 菜色第二批 ==========
    {
        "text": "蔥花煎蛋：外表煎得金黃酥香的蔥花煎蛋，鋪在綠葉上，口感扎實且充滿蛋香與蔥氣，非常受歡迎的家常必點菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-蔥花煎蛋",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "破布子蒸魚：魚肉上方覆蓋著破布子、紅辣椒絲與蔥絲，破布子獨特的甘甜味滲入細緻的魚肉中，是極具地方特色的蒸魚料理。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-破布子蒸魚",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "白斬雞／土雞切塊：肉質緊實的土雞肉切塊，皮色金黃，油脂與膠質豐富，味道香醇，體現了食材的原味，是經典台菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-白斬雞",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "藥膳大蝦：鮮紅的大蝦圍成圓形盤飾，中間加入枸杞等藥膳燉煮，視覺上極具儀式感，蝦肉鮮嫩，湯汁滋補，適合宴客。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-藥膳大蝦",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "涼拌海鮮沙拉：由鮮蝦、花枝圈、洋蔥絲、小黃瓜與彩椒組成的涼拌沙拉，顏色鮮豔豐富，佐以酸甜醬汁，是絕佳的開胃涼菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-涼拌海鮮沙拉",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 菜色第三批 ==========
    {
        "text": "干貝蘆筍沙拉：清蒸干貝撒上黑胡椒粉，搭配苜蓿芽與番茄切片，下方為整齊排列的蘆筍，淋上美乃滋並撒上蔓越莓乾，擺盤極具現代感，口味清爽鮮美。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-干貝蘆筍沙拉",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "炸金針菇與炸蘆筍：裹上薄粉炸至金黃酥脆的金針菇與蘆筍，金針菇呈現花朵般的酥脆質感，口感極佳，是極受歡迎的炸物。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-炸金針菇蘆筍",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "紅燒排骨配青江菜：濃郁醬色的紅燒排骨鋪在鮮綠的青江菜上，撒上白芝麻點綴，肉質軟嫩，醬汁鹹甜適中，是宴席中的亮點大菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-紅燒排骨",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "紅燒肉：將五花肉燉煮至軟糯入味，深色醬汁裹住肉塊，上方點綴香菜，口感油潤，非常適合作為白飯的好搭檔。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-紅燒肉",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "彩椒炒肉片：鮮紅、鮮黃的彩椒與肉片大火快炒，加入蔥段與蒜頭，色澤繽紛，肉片口感彈牙，是一道極為下飯的熱炒料理。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-彩椒炒肉片",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },

    # ========== 菜色與合菜第四批 ==========
    {
        "text": "百香果鮮蝦盅：極具創意的擺盤，將鮮蝦與玉米筍放入百香果殼中，底部鋪上生菜絲，酸甜的百香果風味提升了蝦肉的鮮度，視覺效果精緻優雅，適合宴客。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-百香果鮮蝦盅",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "涼拌花枝海鮮冷盤：豐富的海鮮冷盤，包含鮮蝦、花枝、洋蔥絲、彩椒與小番茄，點綴花椰菜與黑葡萄，口感層次豐富且色彩鮮明，適合宴客。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-涼拌花枝海鮮",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "炒水蓮：清脆的綠色水蓮與少許菇類快炒，色澤鮮綠，口感清脆爽口，是經典的客家熱炒蔬菜，健康清爽。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-炒水蓮",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "香辣酥炸雞：酥炸後的雞肉塊鋪在新鮮綠葉上，上方覆蓋大量蒜酥、辣椒與花生，口感酥脆香辣，是非常道地的熱炒下酒菜。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "菜色-香辣酥炸雞",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
    {
        "text": "滿桌豐盛合菜宴席：美濃莊提供完整的合菜宴席服務，圓桌上可擺滿多道精緻料理，包括大蝦、紅燒排骨、烤鴨、雞湯、蒸魚等，展示了餐廳完整的宴席服務能力，適合喜宴、尾牙、公司聚餐。",
        "source_file": "美濃莊菜色介紹",
        "source_type": "restaurant",
        "page_or_section": "合菜宴席服務",
        "category_hint": ["餐廳推廣"],
        "category": "餐廳推廣",
        "date_processed": TODAY
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "restaurant_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(RESTAURANT_DATA, f, ensure_ascii=False, indent=2)
    print(f"完成！共 {len(RESTAURANT_DATA)} 筆餐廳資料")
    print(f"儲存至：{out_path}")


if __name__ == "__main__":
    main()