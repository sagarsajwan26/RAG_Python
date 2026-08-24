from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
print("model loaded")

text = "fast api is a python web framework"

embedding = model.encode(
    text,
    normalize_embeddings=True,
)

print("embedding shape", embedding.shape)
print("embedding dimension", len(embedding))
print("5 values", embedding[:5])
