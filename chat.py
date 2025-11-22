import streamlit as st
# from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from embedding import getEmbeddingModel

from config import faiss_file_path
import os
from dotenv import load_dotenv
load_dotenv()  # export enviroment variables from .env file


# Initialize the LLM (Large Language Model)
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=500)  # Adjust temperature for creativity (0.0 = very deterministic, 1.0 = more random)

def initializeChat():
     # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

# def displayChatHistory():
    # for message in st.sesss

def handleChat(user_input):
    """
    This function takes in user input and uses RAG (Retrieval Augmented Generation) 
    to generate a response. The RAG technique combines the strengths of traditional 
    information retrieval systems (such as search and vector databases) with the 
    capabilities of generative large language models (LLMs).

    :param user_input: User provided text to generate response
    :return: AI generated response
    """
    response = None
    embedding_model = getEmbeddingModel()
    #  with st.spinner("Application is readying response..."):
    try:
        # Check if FAISS index directory exists and contains the required files
        index_file = os.path.join(faiss_file_path, "index.faiss")
        pkl_file = os.path.join(faiss_file_path, "index.pkl")
        
        if os.path.exists(index_file) and os.path.exists(pkl_file):
            faiss_vector_index = FAISS.load_local(faiss_file_path, 
                                                  embeddings=embedding_model,
                                                  allow_dangerous_deserialization=True)
            # -----Use RAG technique---
            # Load FAISS index having vector stores
            # vector_stores = pickle.load(file)
            # Set up retriever (searches for similar documents)
            retriever = faiss_vector_index.as_retriever(search_kwargs={"k": 3})
            print(f"retriever: {retriever}")
            # Set up RAG Chain (of componenets Retriever & LLM)
            # 1. RetrievalQA is a chain that uses a retriever to find nearest vetctor IDs
            # 2. LangChain fetches the corresponding chunks (from VID-chunks mapping) and Passes them as context to the LLM
            # 3. LLM generates a response based on the context
            rag_chain = RetrievalQA.from_chain_type(
                llm=llm, 
                retriever=retriever,
                return_source_documents=True
                )
            print(f"qa_chain: {rag_chain}")
            response = rag_chain.invoke({"query": user_input})
            print(f"Response received: {response}")
        else:
            st.error("⚠️ No articles processed yet! Please process articles first before asking questions.")
            print(f"FAISS index not found at {faiss_file_path}")
                
    except Exception as e:
        st.error(f"⚠️ Error generating response: {e}")
        print(f"Exception occured: {e}")
        import traceback
        traceback.print_exc()
    return response

                  
