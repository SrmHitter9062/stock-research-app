import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Load the web documents
def loadDocuments(articles_list):
    """
    Loads web documents from the given list of article URLs.

    Args:
        articles_list (list): A list of URLs to load content from.

    Returns:
        list: A list of Document objects containing the content of each article.
    """

    loader = WebBaseLoader(articles_list)
    data = loader.load()
    print("data len-----", len(data))
    #print(data[0].page_content[:500])
    return data

# Split the documents data
def splitDocuments(data):
    """
    Splits the given document data into smaller chunks.

    Args:
        data: A list of Document objects containing the content to be split.

    Returns:
        A list of Document objects, each representing a chunk of the original content.
        The total number of chunks is limited to the first 6.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100 # for maintaining the context
    )
    # Split long documents into smaller chunks
    print('Splitting the web doc data into chunks')
    chunks = text_splitter.split_documents(data)
    print("total chunks: ", len(chunks)) 
    # chunks = chunks[:]
    return chunks

        
def display_vector_store(chunks, embedding_model):
    """
    Prints the vector embeddings of the given chunks to the console.

    Args:
        chunks (list): A list of Document objects to be embedded.
        embedding_model (Embeddings): The embedding model to use.
    """
    print("Here are the vectors")
    for i, chunk in enumerate(chunks):
        embedding_vector = embedding_model.embed_query(chunk.page_content)
        print(f"Id:{i},length: {len(embedding_vector)}, vector: {embedding_vector}\n\n")        


def sendUIResponse(response):
    """
    Displays the UI response based on the provided response data.

    Args:
        response (dict): A dictionary containing the result and source documents.

    Displays:
        - The result header and content if a response is provided.
        - The source article if available.
        - An error message if no response is found.
    """

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
    """
    Extracts the source article from the source documents.

    Args:
        data (dict): The response data containing the source documents.

    Returns:
        str: The source article if available, otherwise None.
    """
    src_documents = data.get("source_documents", [])    
    source_article = None
    for id, doc in enumerate(src_documents):
        print(f"document_id: {id}, metadata: {doc.metadata}")
    source_article = src_documents[0].metadata.get('source')
    return source_article


