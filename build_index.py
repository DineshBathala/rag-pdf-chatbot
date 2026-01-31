from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_and_save_vector_store

def main():
    docs = load_pdf()
    chunks = split_documents(docs)
    create_and_save_vector_store(chunks)

if __name__ == "__main__":
    main()
