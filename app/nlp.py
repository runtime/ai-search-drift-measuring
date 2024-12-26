
#get_ipython().system('pip install -U sentence-transformers')

#todo imports



# Define a passage of text. 
example_text = """In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning). 
A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer. 
A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth.
"""




# Split the sentences in the text. 
sentences = example_text.splitlines()
sentences




# Import the SentenceTransformer class from the sentence_transformers module and use the `all-MiniLM-L6-v2` model.  
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')





# Get the vector embeddings for the sentences. 
search_index = model.encode(sentences)
search_index





#  Each sentence has its own vector.
print(len(search_index))
# Get the vector length for the first sentence
print(len(search_index[0]))





# Create a query and encode the query with the model. 
query = "Transformers use tokenization"
search_query = model.encode([query])
# Get the first 50 embeddings of the query. 
search_query[0][0:50]





# The length of the vector embeddings is the same as each sentence embedding.
len(search_query[0])





# Import the util module from the sentence_transformers class, 
# which will be used to determine the similarity measures. 
from sentence_transformers import util





# Loop through the sentence embeddings and compare each sentence embedding with our query embedding.
for i in range(len(search_index)):
  index_embedding = search_index[i]
  cosine_similarity_score = util.cos_sim(index_embedding, search_query)
  print(f"Query: {query}")
  print(f"Sentence {i+1}: {sentences[i]}")
  print(f"Similarity score: {cosine_similarity_score}")
  print()











get_ipython().system('pip install -U sentence-transformers')





get_ipython().system('pip install -U sentence-transformers')





# Define a passage of text. 
example_text = """In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters (such as in a computer program or web page) into a sequence of lexical tokens (strings with an assigned and thus identified meaning). 
A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner, although scanner is also a term for the first stage of a lexer. 
A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages, and so forth.
"""


# Split the sentences in the text. 
sentences = example_text.splitlines()
sentences


# Import the SentenceTransformer class from the sentence_transformers module and use the `all-MiniLM-L6-v2` model.  
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


# Get the vector embeddings for the sentences. 
search_index = model.encode(sentences)
search_index

#  Each sentence has its own vector.
print(len(search_index))
# Get the vector length for the first sentence
print(len(search_index[0]))

# Create a query and encode the query with the model. 
query = "Transformers use tokenization"
search_query = model.encode([query])
# Get the first 50 embeddings of the query. 
search_query[0][0:50]

# The length of the vector embeddings is the same as each sentence embedding.
len(search_query[0])


# Import the util module from the sentence_transformers class, 
# which will be used to determine the similarity measures. 
from sentence_transformers import util


# Loop through the sentence embeddings and compare each sentence embedding with our query embedding.
for i in range(len(search_index)):
  index_embedding = search_index[i]
  cosine_similarity_score = util.cos_sim(index_embedding, search_query)
  print(f"Query: {query}")
  print(f"Sentence {i+1}: {sentences[i]}")
  print(f"Similarity score: {cosine_similarity_score}")
  print()




