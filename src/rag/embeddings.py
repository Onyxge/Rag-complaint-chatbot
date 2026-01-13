import pandas as pd
import chromadb
import os

# --- Configuration ---
PARQUET_PATH = "/kaggle/working/complaint_embeddings.parquet"
CHROMA_PATH = "/kaggle/working/"

print(f"🚀 Starting Fast Load from {PARQUET_PATH}...")

# 1. Load Parquet
df = pd.read_parquet(PARQUET_PATH)
print(f"✅ Loaded Dataframe: {len(df)} rows")

# 2. Initialize ChromaDB
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Reset collection to avoid duplicates
try:
    client.delete_collection("complaint_vectors_full")
    print("Deleted old collection.")
except:
    pass

collection = client.create_collection(
    name="complaint_vectors_full",
    metadata={"hnsw:space": "cosine"}
)

# 3. Batch Insert
BATCH_SIZE = 5000
total_rows = len(df)

ids, embeddings, documents, metadatas = [], [], [], []

print(f"Pushing data to ChromaDB in batches of {BATCH_SIZE}...")

for index, row in df.iterrows():
    # A. Guaranteed-unique ID
    ids.append(f"{row['id']}_{index}")

    # B. Embedding (numpy → list)
    embeddings.append(row['embedding'].tolist())

    # C. Document text
    documents.append(row['document'])

    # D. Clean metadata
    meta_raw = row['metadata']
    clean_meta = {
        "product": meta_raw.get("product") or meta_raw.get("product_category") or "Unknown",
        "complaint_id": str(meta_raw.get("complaint_id", "")),
        "issue": meta_raw.get("issue", "")
    }
    metadatas.append(clean_meta)

    # E. Batch commit
    if len(ids) >= BATCH_SIZE:
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
        ids, embeddings, documents, metadatas = [], [], [], []

        if index % 50000 == 0:
            print(f"Indexed {index} / {total_rows}...")

# Final batch
if ids:
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )

# Optional but recommended
client.persist()

print(f"🎉 Success! Vector Store Ready. Total Count: {collection.count()}")
