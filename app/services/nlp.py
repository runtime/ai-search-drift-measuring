
#get_ipython().system('pip install -U sentence-transformers')
from sentence_transformers import util


# Define a passage of text.
example_text = """In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning).
A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer.
A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth.
"""

# Split the sentences in the text.
sentences = example_text.splitlines()
#sentences


# Import the SentenceTransformer class from the sentence_transformers module and use the `all-MiniLM-L6-v2` model.
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


# Get the vector embeddings for the sentences.
search_index = model.encode(sentences)
#print(search_index)



#  Each sentence has its own vector.
print(len(search_index))
# Get the vector length for the first sentence
print(len(search_index[0]))

#start
# Define potential answers to the query
potential_answers = [
    "Transformers are important for AI search.",
    "Tokenization converts text into tokens.",
    "Attention mechanisms are used in transformers."
]

# Create a query and encode the query with the model.

query = "Why are transformers important for search?"
query_embedding = model.encode([query])
answers_embeddings = model.encode(potential_answers)

# Loop through each potential answer and calculate cosine similarity
for i, answer_embedding in enumerate(answers_embeddings):
    cosine_similarity_score = util.cos_sim(answer_embedding, query_embedding)
    print(f"Query: {query}")
    print(f"Potential Answer {i + 1}: {potential_answers[i]}")
    print(f"Similarity score: {cosine_similarity_score.item()}")
    print()




# Loop through the sentence embeddings and compare each sentence embedding with our query embedding.
# for i in range(len(search_index)):
#   index_embedding = search_index[i]
#   cosine_similarity_score = util.cos_sim(index_embedding, search_query)
#   print(f"Query: {query}")
#   print(f"Sentence {i+1}: {sentences[i]}")
#   print(f"Similarity score: {cosine_similarity_score}")
#   print()


