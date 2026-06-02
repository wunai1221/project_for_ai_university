"""
向量化程式
功能：讀取所有 JSON 資料，向量化後存進 Chroma 向量資料庫
輸出位置：rag/vectorstore/
"""

import json
import os
import glob
import chromadb
from sentence_transformers import SentenceTransformer

# ============================================================
# 設定區
# ============================================================
# 資料來源資料夾
RAW_DIRS = [
    os.path.join(os.path.dirname(__file__), "../data/raw/websites"),
    os.path.join(os.path.dirname(__file__), "../data/raw/pptx"),
    os.path.join(os.path.dirname(__file__), "../data/raw/docx"),
    os.path.join(os.path.dirname(__file__), "../data/raw/restaurant"),
    os.path.join(os.path.dirname(__file__), "../data/raw/manual"),
    os.path.join(os.path.dirname(__file__), "../data/raw/manual_ppt"),
]

# 向量庫輸出位置
VECTORSTORE_DIR = os.path.join(os.path.dirname(__file__), "../vectorstore")

# Embedding 模型（支援中文）
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
# ============================================================


def load_all_data() -> list[dict]:
    """讀取所有 JSON 檔案，跳過合併檔避免重複"""
    all_data = []
    for raw_dir in RAW_DIRS:
        json_files = glob.glob(os.path.join(raw_dir, "*.json"))
        for filepath in json_files:
            filename = os.path.basename(filepath)
            if filename.startswith("_all_"):
                continue
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                all_data.extend(data)
            print(f"  載入：{filename}（{len(data)} 筆）")
    return all_data


def build_vectorstore():
    print("載入資料中...")
    all_data = load_all_data()
    print(f"\n共載入 {len(all_data)} 筆資料")

    print("\n載入 Embedding 模型中（第一次會下載，請稍候）...")
    model = SentenceTransformer(MODEL_NAME)
    print("模型載入完成！")

    print("\n初始化向量資料庫...")
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
    client = chromadb.PersistentClient(path=VECTORSTORE_DIR)

    try:
        client.delete_collection("rag_collection")
    except:
        pass
    collection = client.create_collection("rag_collection")

    print("開始向量化並存入資料庫...")
    batch_size = 10
    for i in range(0, len(all_data), batch_size):
        batch = all_data[i:i + batch_size]

        texts = [item["text"] for item in batch]
        embeddings = model.encode(texts).tolist()

        ids = [f"doc_{i + j}" for j in range(len(batch))]
        metadatas = [
            {
                "source_file": item.get("source_file", ""),
                "source_type": item.get("source_type", ""),
                "page_or_section": item.get("page_or_section", ""),
                "category_hint": str(item.get("category_hint", "")),
                "category": item.get("category", ""),
            }
            for item in batch
        ]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

        print(f"  進度：{min(i + batch_size, len(all_data))}/{len(all_data)} 筆")

    print(f"\n完成！向量資料庫已儲存至：{VECTORSTORE_DIR}")
    print(f"共存入 {collection.count()} 筆資料")


if __name__ == "__main__":
    build_vectorstore()