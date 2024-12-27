from fastapi import FastAPI, HTTPException
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel

app = FastAPI()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
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
@app.post("/store")
def store_embedding(sentence: str):
    embedding = model.encode(sentence).tolist()
    cursor.execute(
        "INSERT INTO embeddings (sentence, embedding) VALUES (%s, %s) RETURNING id",
        (sentence, embedding)
    )
    conn.commit()
    return {"id": cursor.fetchone()[0], "message": "Embedding stored successfully!"}

# Query embeddings
@app.post("/query", response_model=list[EmbeddingResponse])
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
