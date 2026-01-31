from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

FAISS_PATH = "faiss_index"

def create_and_save_vector_store(chunks):
    embeddings = OllamaEmbeddings(model="mistral")
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(FAISS_PATH)
    print("FAISS index saved to disk")

def load_vector_store():
    embeddings = OllamaEmbeddings(model="mistral")
    return FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
