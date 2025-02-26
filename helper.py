

def display_vector_store(chunks, embedding_model):
    print("Here are the vectors")
    for i, chunk in enumerate(chunks):
        embedding_vector = embedding_model.embed_query(chunk.page_content)
        print(f"Id:{i},length: {len(embedding_vector)}, vector: {embedding_vector}\n\n")        
