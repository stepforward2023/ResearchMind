import chromadb
from sentence_transformers import SentenceTransformer

query = "What is Transformer architecture?"

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

query_embedding = model.encode(query).tolist()

client = chromadb.PersistentClient(
    path="data/vectordb"
)

collection = client.get_collection(
    name="researchmind"
)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"][0])