from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

test_text = "Attention is all you need"

embedding = model.encode(test_text)

print("Embedding Generated!")
print(f"Shape: {embedding.shape}")
