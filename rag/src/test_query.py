"""
測試查詢程式
功能：輸入問題，看向量庫能不能找到相關資料
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer

VECTORSTORE_DIR = os.path.join(os.path.dirname(__file__), "../vectorstore")
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

model = SentenceTransformer(MODEL_NAME)
client = chromadb.PersistentClient(path=VECTORSTORE_DIR)
collection = client.get_collection("rag_collection")

print("向量資料庫載入完成！輸入問題來測試（輸入 exit 離開）")
print(f"資料庫共有 {collection.count()} 筆資料\n")

while True:
    question = input("請輸入問題：").strip()
    if question.lower() == "exit":
        break

    embedding = model.encode([question]).tolist()
    results = collection.query(
        query_embeddings=embedding,
        n_results=3
    )

    print("\n--- 找到最相關的 3 筆資料 ---")
    for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
        print(f"\n第 {i+1} 筆")
        print(f"來源：{meta['source_file']} / {meta['page_or_section']}")
        print(f"內容：{doc[:150]}...")
    print("---\n")
    