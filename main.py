import streamlit as st
import time
import pickle
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI


from embedding import getEmbeddingModel
from helper import display_vector_store
from chat import handleChat
from config import faiss_file_path
from helper import sendUIResponse

from dotenv import load_dotenv
load_dotenv()  # export enviroment variables from .envv file

st.title("Stock research Bot")
st.sidebar.title("Stock article")

articles_list = []
for k in range(3):
    article = st.sidebar.text_input(f"Article {k+1}")
    articles_list.append(article)

main_placeholder = st.empty()
process_artcle_clicked = st.sidebar.button("Process Articles")
user_input = None
if process_artcle_clicked:
    main_placeholder.text("Web Documment Loading...Started...✅✅✅")
    print('Articles are being processed...')
    # loader = UnstructuredURLLoader(urls=articles_list)
    # Load the web document
    print("Loading the web documents")
    loader = WebBaseLoader(articles_list)
    data = loader.load()
    #print(data[0].page_content[:500])

    main_placeholder.text("Documment Splitting in chunks...Started...✅✅✅")
    # Create a text splitter instance    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100
    )
    # Split long documents into smaller chunks
    print('Splitting the web doc data into chunks')
    chunks = text_splitter.split_documents(data)
    print("total chunks: ", len(chunks))   
    chunks = chunks[:6]
  
    print("chunk_list: ", chunks[0])   
    embedding_model = getEmbeddingModel()

    # display_vector_store(chunks, embedding_model);  
       
    # --------Tasks: Embedding, FAISS index creation--------
    # 1. Internally, below uses the embedding_model to generate the embeddings for the text in each Document object or chunk
    # 2. Then it takes these newly created embeddings and stores them in a FAISS index. The FAISS index is a data structure optimized for fast similarity search.    
    try:
        main_placeholder.text("Embedding...Started...✅✅✅")
        faiss_vector_index = FAISS.from_documents(chunks, embedding_model)        
        time.sleep(2)
    
        #------ Save the FAISS index-----
        faiss_vector_index.save_local(faiss_file_path)        
        main_placeholder.text("Articles are processed...Now ask question...✅✅✅")         
       
    except Exception as e:
        print(f"Error saving FAISS index: {e}")

user_input = st.chat_input("Type your Question:")  
if user_input:
    with st.spinner("Stock research Boot is readying response..."):
        resp = handleChat(user_input) 
    # print(f"response: {resp}")
    sendUIResponse(resp)