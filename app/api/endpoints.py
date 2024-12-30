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

@router.post("/query")
def analyze_query():
    try:
        # Step 1: Hardcoded answers simulating LLM responses
#         potential_answers = [
#             "tokenization is the process of converting a sequence of characters into tokens.",
#             "A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner.",
#             "Transformers are provided in a number of python machine learning libraries."
#         ]

        potential_answers = [
            "A tokenizer can also be called a lexer but there are some distinct differences.",
            "A tokenizer can take any string and turns it into a series of tokens or values that have context to one another",
            "A tokenizer is critical to creating a RAG or other AI Search as the method of finding relevant matches between queries and vectors in the data set."
        ]

        results = []

        # Step 2: Fetch corpus embeddings from the DB
        cursor.execute("SELECT text, embedding FROM embeddings")
        rows = cursor.fetchall()

        for answer in potential_answers:
            # Encode the simulated answer
            answer_embedding = model.encode(answer)

            # Step 3: Compare to each corpus entry
            max_similarity = 0
            closest_corpus_text = None
            for text, serialized_embedding in rows:
                # Deserialize the embedding
                corpus_embedding = pickle.loads(serialized_embedding)

                # Calculate similarity
                similarity = util.cos_sim(answer_embedding, corpus_embedding)[0][0].item()
                if similarity > max_similarity:
                    max_similarity = similarity
                    closest_corpus_text = text

            # Add results for this answer
            results.append({
                "answer": answer,
                "most_similar_corpus_text": closest_corpus_text,
                "similarity": max_similarity,
                "flagged": max_similarity < 0.7  # Example threshold for drift
            })

        # Step 4: Log results to `drift_scores`
        for result in results:
            cursor.execute(
                "INSERT INTO drift_scores (query, response, similarity, flagged) VALUES (%s, %s, %s, %s)",
                ("Simulated Query", result["answer"], result["similarity"], result["flagged"])
            )
        conn.commit()

        # Step 5: Return results
        return {"query": "Simulated Query", "results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@router.get("/drift")
def get_drift_scores():
    try:
        # Fetch all drift scores
        cursor.execute("SELECT id, query, response, similarity, flagged, created_at FROM drift_scores ORDER BY created_at DESC")
        rows = cursor.fetchall()

        # Format results for API response
        results = [
            {
                "id": row[0],
                "query": row[1],
                "response": row[2],
                "similarity": row[3],
                "flagged": row[4],
                "created_at": row[5].isoformat(),
            }
            for row in rows
        ]

        return {"scores": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching drift scores: {str(e)}")

