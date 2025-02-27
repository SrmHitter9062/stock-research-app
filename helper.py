import streamlit as st

def display_vector_store(chunks, embedding_model):
    print("Here are the vectors")
    for i, chunk in enumerate(chunks):
        embedding_vector = embedding_model.embed_query(chunk.page_content)
        print(f"Id:{i},length: {len(embedding_vector)}, vector: {embedding_vector}\n\n")        


def sendUIResponse(response):
    if response:
        st.header("Result:")
        st.write(response['result'])
        source_article = getSourceArticle(response)
        if source_article:
            st.subheader("Source:")
            st.write(source_article)
    else:
        st.header("Result:")
        st.write("Sorry !! Could not find answer")


def getSourceArticle(data):
    src_documents = data.get("source_documents", [])    
    source_article = None
    for id, doc in enumerate(src_documents):
        print(f"document_id: {id}, metadata: {doc.metadata}")
    source_article = src_documents[0].metadata.get('source')
    return source_article