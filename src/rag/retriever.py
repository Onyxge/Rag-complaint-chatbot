import chromadb
from sentence_transformers import SentenceTransformer
from huggingface_hub import cached_download

CHROMA_PATH = "ChromaDB/vector_store"
COLLECTION_NAME = "chroma"

class ComplaintRetriever:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_PATH)
        try:
            self.collection = self.client.get_collection(COLLECTION_NAME)
        except Exception:
            raise RuntimeError(
                f"Chroma collection '{COLLECTION_NAME}' not found. "
                f"Did you run the indexing step?"
            )

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def search(self, query: str, product: str | None = None, top_k: int = 5):
        query_embedding = self.model.encode(query).tolist()

        where_clause = {"product": product} if product else None

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_clause,
            include=["documents", "metadatas"]
        )

        retrieved = []
        for i in range(len(results["documents"][0])):
            retrieved.append({
                "text": results["documents"][0][i],
                "metadata": results["metadatas"][0][i]
            })

        return retrieved
