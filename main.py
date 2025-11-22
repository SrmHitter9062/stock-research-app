import streamlit as st
import time
from langchain_community.vectorstores import FAISS
# from langchain_community.llms import OpenAI


from embedding import getEmbeddingModel
from helper import display_vector_store
from chat import handleChat
from config import faiss_file_path, steps_msg
from helper import loadDocuments, splitDocuments, sendUIResponse

from dotenv import load_dotenv
load_dotenv()  # export enviroment variables from .env file

st.markdown("### 🔍📉 AI Stock Researcher – Insights at Your Fingertips")
st.sidebar.title("📌 Stock articles")
main_placeholder = st.empty() 
# Function to add a processing step and update the UI
def add_step(msg, t=0):    
    st.sidebar.text(msg)
    time.sleep(t)


articles_list = []
for k in range(3):
    article = st.sidebar.text_input(f"Article {k+1}")
    articles_list.append(article)


process_artcle_clicked = st.sidebar.button("Process Articles")

if process_artcle_clicked:
    # Filter out empty URLs
    articles_list = [url.strip() for url in articles_list if url.strip()]
    
    if not articles_list:
        st.sidebar.error("⚠️ Please provide at least one article URL!")
    else:
        with st.spinner("Processing articles... Please wait ⏳"):        
            # 1. Load the web documents
            print("Loading the web documents")
            try:
                data = loadDocuments(articles_list=articles_list)
                if not data or len(data) == 0:
                    st.sidebar.error("⚠️ Failed to load articles. Please check the URLs.")
                else:
                    add_step(steps_msg[1], 1)        
                    
                    # 2. Document splitting        
                    chunks = splitDocuments(data)
                    
                    if not chunks or len(chunks) == 0:
                        st.sidebar.error("⚠️ No content found in articles to process.")
                    else:
                        add_step(steps_msg[2])
                        print("chunk_list: ", chunks[0] if chunks else "No chunks")   
                        
                        embedding_model = getEmbeddingModel()

                        # display_vector_store(chunks, embedding_model);  
                        
                        # 3.--------Tasks: Embedding, FAISS index creation--------
                        # 3.1. Uses the embedding_model to create vector embeddings for each document chunk.
                        # 3.2. Stores these embeddings (vector ID and vector) in a FAISS index for efficient similarity search and retrieval.
                        try:            
                            faiss_vector_index = FAISS.from_documents(chunks, embedding_model)        
                            # time.sleep(1)
                            # #------ Save the FAISS index-----
                            faiss_vector_index.save_local(faiss_file_path)        
                            add_step(steps_msg[3], 1)         
                            st.sidebar.success("✅ Articles processed successfully! You can now ask questions.")
                        except Exception as e:
                            st.sidebar.error(f"⚠️ Error creating FAISS index: {e}")
                            print(f"Error saving FAISS index: {e}")
                        
                        add_step(steps_msg[4], 1)
            except Exception as e:
                st.sidebar.error(f"⚠️ Error loading articles: {e}")
                print(f"Error loading documents: {e}")        

user_input = st.chat_input("Type your Question:") 
if user_input:
    with st.spinner("Readying your response..."):
        resp = handleChat(user_input)
    # print(f"response: {resp}")
    sendUIResponse(resp)
