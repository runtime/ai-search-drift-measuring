import psycopg2
import pickle
from sentence_transformers import SentenceTransformer
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

# Define the corpus
example = """In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning).
A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer. A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth."""

# Split the sentences into a list
#corpus = example.splitlines()

#tokenize the text into sentences using nltk sent_tokenize
corpus = sent_tokenize(example)

print(f"Stored sentence: {corpus}")

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

# Add corpus to the database
for sentence in corpus:
    try:
        # Encode the sentence
        embedding = model.encode(sentence)
        serialized_embedding = pickle.dumps(embedding)

        print(f"Storing sentence: {sentence}")

        # Insert into database
        cursor.execute(
            "INSERT INTO embeddings (text, embedding) VALUES (%s, %s)",
            (sentence, serialized_embedding)
        )

        print(f"Stored sentence: {sentence}")
    except Exception as e:
        print(f"Error storing sentence: {sentence} -> {str(e)}")
        continue

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Corpus added to the database!")
