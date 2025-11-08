

import chromadb
from embedding import get_embedding
import time


chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="pdf_chunks")

def add_chunks(chunks):
    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk)
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[emb]
        )
        time.sleep(0.1)  

def retrieve_context(query, top_k=3):
    """Retrieve top-k most relevant chunks for a query"""
    q_emb = get_embedding(query)
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k
    )
    return results["documents"][0]
