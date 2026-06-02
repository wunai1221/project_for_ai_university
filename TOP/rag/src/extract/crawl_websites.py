"""
網站爬蟲程式
功能：爬取指定網站的文字內容，清除雜訊後儲存成 JSON 格式
輸出位置：rag/data/raw/websites/
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from datetime import datetime
from urllib.parse import urljoin, urlparse

# ============================================================
# 設定區
# ============================================================
WEBSITES = [
    {
        "name": "鉅昕鋼鐵官網",
        "url": "https://www.khh73.com.tw/index.html",
        "category_hint": ["鋼筋加工", "鋼構工程", "鋼材買賣及加工"],
        "skip_url_keywords": []
    },
    {
        "name": "旗美農官網",
        "url": "https://chimeiagr.com.tw/feq/index.aspx",
        "category_hint": ["農產品推銷"],
        "skip_url_keywords": ["productlist", "product.aspx", "cart", "login", "notice", "nomemberorder", "terms", "privacy"]
    },
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw/websites")
NOISE_TAGS = ["nav", "header", "footer", "script", "style", "aside", "form", "button"]
<<<<<<< HEAD
MAX_PAGES = 80
=======
MAX_PAGES = 20
>>>>>>> 4745f2536beadefc9b2b8e5a7184942db2d98937
# ============================================================


def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def extract_text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in NOISE_TAGS:
        for element in soup.find_all(tag):
            element.decompose()

    main_content = (
        soup.find("main") or
        soup.find(id="content") or
        soup.find(id="main") or
        soup.find(class_="content") or
        soup.find("article") or
        soup.find("body")
    )

    if main_content:
        text = main_content.get_text(separator="\n")
    else:
        text = soup.get_text(separator="\n")

    return clean_text(text)


def get_internal_links(html: str, base_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    base_domain = urlparse(base_url).netloc
    links = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)

        if parsed.netloc == base_domain and parsed.scheme in ("http", "https"):
            clean_url = parsed._replace(fragment="").geturl()
            links.add(clean_url)

    return list(links)


def crawl_website(site: dict) -> list[dict]:
    name = site["name"]
    start_url = site["url"]
    category_hint = site.get("category_hint", "")
    skip_keywords = site.get("skip_url_keywords", [])

    print(f"\n開始爬取：{name} ({start_url})")

    visited = set()
    to_visit = [start_url]
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
    }

    while to_visit and len(visited) < MAX_PAGES:
        url = to_visit.pop(0)
        if url in visited:
            continue

        # 跳過不需要的頁面
        if any(keyword in url for keyword in skip_keywords):
            print(f"    → 跳過：{url}")
            visited.add(url)
            continue

        try:
            print(f"  爬取頁面：{url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding = response.apparent_encoding
            response.raise_for_status()

            html = response.text
            text = extract_text_from_html(html)

            if len(text) < 50:
                print(f"    → 內容太少，跳過")
                visited.add(url)
                continue

            results.append({
                "text": text,
                "source_file": name,
                "source_type": "web",
                "url": url,
                "page_or_section": url,
                "category_hint": category_hint,
                "category": "",
                "date_processed": datetime.now().strftime("%Y-%m-%d")
            })

            new_links = get_internal_links(html, start_url)
            for link in new_links:
                if link not in visited:
                    to_visit.append(link)

            visited.add(url)
            time.sleep(1)

        except Exception as e:
            print(f"    → 爬取失敗：{e}")
            visited.add(url)

    print(f"  完成，共爬取 {len(results)} 頁")
    return results


def save_results(results: list[dict], site_name: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{site_name.replace(' ', '_')}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"  已儲存：{filepath}（共 {len(results)} 筆）")


def main():
    all_results = []

    for site in WEBSITES:
        results = crawl_website(site)
        save_results(results, site["name"])
        all_results.extend(results)

    merged_path = os.path.join(OUTPUT_DIR, "_all_websites.json")
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\n全部完成！共爬取 {len(all_results)} 筆資料")
    print(f"合併檔案：{merged_path}")


if __name__ == "__main__":
    main()