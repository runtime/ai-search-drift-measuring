from fastapi import APIRouter, HTTPException
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
import pickle
import json

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
import pickle  # For serializing embeddings into bytea

@router.post("/store")
def store_embedding(sentence: str):
    try:
        # sentence = sentence
        if not sentence:
            raise HTTPException(status_code=400, detail="Sentence is required")


        #return {"message": f"Embedding stored successfully for sentence: {sentence}"}
        # Generate embedding using the SentenceTransformer model
        embedding = model.encode(sentence)
        serialized_embedding = pickle.dumps(embedding)  # Serialize the embedding

        # Store the sentence and embedding in the database
        cursor.execute(
            "INSERT INTO embeddings (text, embedding) VALUES (%s, %s) RETURNING id",
            (sentence, serialized_embedding)
        )
        conn.commit()

        # Get the ID of the inserted record
        record_id = cursor.fetchone()[0]

        return {"id": record_id, "message": f"Embedding stored successfully for sentence: {sentence}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error storing embedding: {str(e)}")



# Query embeddings

@router.post("/query", response_model=list[EmbeddingResponse])
def query_embedding(query: Query):
    try:
        # Encode the query text
        query_embedding = model.encode(query.text)

        # Retrieve all embeddings from the database
        cursor.execute("SELECT text, embedding FROM embeddings")
        rows = cursor.fetchall()

        results = []
        for text, serialized_embedding in rows:
            # Deserialize the embedding
            stored_embedding = pickle.loads(serialized_embedding)

            # Calculate cosine similarity
            similarity = util.cos_sim(query_embedding, stored_embedding)[0][0].item()

            # Append the result
            results.append({"sentence": text, "similarity": similarity})

        # Sort results by similarity in descending order
        results = sorted(results, key=lambda x: x["similarity"], reverse=True)

        # Return the top 5 most similar results
        return results[:5]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying embeddings: {str(e)}")
