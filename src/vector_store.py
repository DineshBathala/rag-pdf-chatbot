import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

load_dotenv()

INDEX_NAME = "rag-pdf-index"


def create_and_save_vector_store(chunks):
    print("Connecting to Pinecone...")

    pc = Pinecone(api_key=os.getenv("pcsk_2xTjs5_T4qjhrxmoMwbXB4Rmj3ogiVHsLCHve1VsGGFrgMvKa8g376RtEGAgxncf5Dh3gY"))

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=INDEX_NAME,
    )

    print("Uploaded embeddings to Pinecone")


def load_vector_store():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    return PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings,
    )
