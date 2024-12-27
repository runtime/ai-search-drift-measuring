from sentence_transformers import SentenceTransformer
import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("NumPy version:", tf.__version__)

model = SentenceTransformer('all-MiniLM-L6-v2')
print("SentenceTransformer model loaded successfully!")
