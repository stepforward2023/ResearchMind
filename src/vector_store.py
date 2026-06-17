import chromadb
from sentence_transformers import SentenceTransformer

# Create database

client = chromadb.PersistentClient(
    path="data/vectordb"
)

collection = client.get_or_create_collection(
    name="researchmind"
)

# Load embedding model

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Sample text

text = "Attention is all you need"

embedding = model.encode(text).tolist()

# Store in ChromaDB

collection.add(
    ids=["chunk_1"],
    documents=[text],
    embeddings=[embedding]
)

print("Stored Successfully!")
results = collection.query(
    query_embeddings=[embedding],
    n_results=1
)

print(results)

