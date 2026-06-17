import fitz
import chromadb

from sentence_transformers import SentenceTransformer
from recursive_chunker import recursive_chunk_text

# Read PDF

pdf_path = "data/papers/paper.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

# Chunk

chunks = recursive_chunk_text(full_text)

print(f"Total Chunks: {len(chunks)}")

# Embedding Model

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# ChromaDB

client = chromadb.PersistentClient(
    path="data/vectordb"
)

collection = client.get_or_create_collection(
    name="researchmind"
)

# Store Chunks

for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk).tolist()

    collection.add(
        ids=[f"chunk_{i}"],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Stored Successfully!")