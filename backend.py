import os
import openai
from pinecone import Pinecone, ServerlessSpec
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.pinecone import PineconeVectorStore

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Get the index
pinecone_index = pc.Index("bini")

# Initialize VectorStore
vector_store = PineconeVectorStore(
    pinecone_index=pinecone_index,
    add_sparse_vector=True,
)

# Initialize OpenAI Embedding Model
embedding_model = "text-embedding-3-small"  # Replace with the actual model name
embed_model = OpenAIEmbedding(api_key=openai.api_key, model=embedding_model)

# Load Storage Context
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Load the index from the vector store
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, embed_model=embed_model)

# Create a query engine
query_engine = index.as_query_engine(vector_store_query_mode="hybrid")