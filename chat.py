import streamlit as st
# from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from config import faiss_file_path
import os, pickle
from dotenv import load_dotenv
load_dotenv()  # export enviroment variables from .envv file
# Initialize the LLM (Large Language Model)
llm = ChatOpenAI(model="gpt-4o-mini",
                 temperature=0.9,
                 max_tokens=500)  # Adjust temperature for creativity (0.0 = very deterministic, 1.0 = more random)

def initializeChat():
     # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

# def displayChatHistory():
    # for message in st.sesss

def handleChat(user_input):
    #  with st.spinner("Application is readying response..."):
    if os.path.exists(faiss_file_path):
         with open(faiss_file_path, 'rb') as file:
            try:
                # -----Use RAG technique---
                # Load FAISS index having vector stores
                vector_stores = pickle.load(file)
                # Set up retriever (searches for similar documents)
                retriever = vector_stores.as_retriever(search_kwargs={"k": 2})
                print(f"retriever: {retriever}")
                # Set up RAG Chain (Retriever + LLM)
                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm, 
                    retriever=retriever,
                    return_source_documents=True
                    )
                print(f"qa_chain: {qa_chain}")
                response = qa_chain.invoke(user_input)
                print(f"response: {response}")
                displayResult(response)
                
            except Exception as e:
                print(f"Exception occured: {e}")
                st.header("Answer")
                st.write("Sorry !! Could not find answer")


def displayResult(response):
    st.header("Result:")
    st.write(response['result'])
    source_article = getSourceArticle(response)
    if source_article:
        st.subheader("Source:")
        st.write(source_article)


def getSourceArticle(data):
    src_documents = data.get("source_documents", [])    
    source_article = None
    for id, doc in enumerate(src_documents):
        print(f"document_id: {id}, metadata: {doc.metadata}")
    source_article = src_documents[0].metadata.get('source')
    return source_article

                  
