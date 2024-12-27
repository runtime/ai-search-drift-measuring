from fastapi import APIRouter, HTTPException
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel

router = APIRouter()

print("API module loaded!")

# Test endpoint
@router.get("/test")
def test_endpoint():
    return {"message": "Test endpoint works!"}

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="aisearch",
    user="home",
    password="12345",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define input/output schemas
class Query(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    sentence: str
    similarity: float

# Store embeddings
@router.post("/store")
def store_embedding(sentence: str):
    return {"message": f"Received sentence: {sentence}"}

# Query embeddings
@router.post("/query", response_model=list[EmbeddingResponse])
def query_embedding(query: Query):
    cursor.execute("SELECT id, sentence, embedding FROM embeddings")
    rows = cursor.fetchall()
    results = []

    query_embedding = model.encode(query.text)
    for _, sentence, embedding in rows:
        similarity = util.cos_sim(query_embedding, np.array(embedding))[0][0]
        results.append({"sentence": sentence, "similarity": similarity.item()})

    # Sort by similarity
    results = sorted(results, key=lambda x: x["similarity"], reverse=True)
    return results[:5]
