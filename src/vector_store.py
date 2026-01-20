import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(chunks):
    """
    Creates a FAISS vector store from document chunks
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set")

    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store
