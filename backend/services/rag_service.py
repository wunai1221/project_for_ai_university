import chromadb
from sentence_transformers import SentenceTransformer

# 載入 Embedding 模型（跟 A 同學一樣的）
_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# 載入 Chroma 向量資料庫（使用相對路徑，便於 git 打包）
_client = chromadb.PersistentClient(path="rag/vectorstore")


def search(query: str, top_k: int = 5) -> str:
    """查詢向量庫，回傳最相關的段落文字（已移除 category 過濾）"""

    # 取得所有 collection 並合併結果
    all_results = []

    for col_name in _client.list_collections():
        collection = _client.get_collection(
            name=col_name.name if hasattr(col_name, 'name') else col_name,
            embedding_function=None,
        )

        # 手動算 embedding
        query_embedding = _model.encode(query).tolist()

        # 查詢參數（不再使用 category where 過濾）
        query_params = {
            "query_embeddings": [query_embedding],
            "n_results": top_k,
        }

        try:
            results = collection.query(**query_params)
            if results["documents"] and results["documents"][0]:
                for doc, dist in zip(results["documents"][0], results["distances"][0]):
                    all_results.append((dist, doc))
        except Exception as e:
            print(f"查詢 collection {col_name} 失敗: {e}")
            continue

    # 按距離排序，取前 top_k
    all_results.sort(key=lambda x: x[0])
    top_docs = [doc for _, doc in all_results[:top_k]]

    if not top_docs:
        return ""

    return "\n\n---\n\n".join(top_docs)