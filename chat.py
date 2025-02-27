import streamlit as st
# from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from embedding import getEmbeddingModel

from config import faiss_file_path
import os
from dotenv import load_dotenv
load_dotenv()  # export enviroment variables from .envv file


# Initialize the LLM (Large Language Model)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9,
    max_tokens=500)  # Adjust temperature for creativity (0.0 = very deterministic, 1.0 = more random)

def initializeChat():
     # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

# def displayChatHistory():
    # for message in st.sesss

def handleChat(user_input):
    response = None
    embedding_model = getEmbeddingModel()
    #  with st.spinner("Application is readying response..."):
    try:
        if os.path.exists(faiss_file_path):
            faiss_vector_index = FAISS.load_local(faiss_file_path, 
                                                  embeddings=embedding_model,
                                                  allow_dangerous_deserialization=True)
            # -----Use RAG technique---
            # Load FAISS index having vector stores
            # vector_stores = pickle.load(file)
            # Set up retriever (searches for similar documents)
            retriever = faiss_vector_index.as_retriever(search_kwargs={"k": 2})
            print(f"retriever: {retriever}")
            # Set up RAG Chain (Retriever + LLM)
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm, 
                retriever=retriever,
                return_source_documents=True
                )
            print(f"qa_chain: {qa_chain}")
            response = qa_chain.invoke(user_input)
                
    except Exception as e:
        print(f"Exception occured: {e}")       
    return response

                  
