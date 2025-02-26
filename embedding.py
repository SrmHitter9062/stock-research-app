# from langchain_openai import OpenAIEmbeddings # paid
# from langchain.embeddings import HuggingFaceEmbeddings # Using for free embedding 
from langchain_huggingface import HuggingFaceEmbeddings

def getEmbeddingModel():
    # Initialize hugging face embeddings instance
    # embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    model_name = "sentence-transformers/all-MiniLM-L6-v2" 
    model_kwargs = {'device':'cpu'} # Create a dictionary with model configuration options, specifying to use the CPU for computations
    encode_kwargs = {'normalize_embeddings': False}  # Default is False, Set to True for normalized embeddings, True means that the length (magnitude) of each embedding vector will be 1. 
    
    embedding_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embedding_model