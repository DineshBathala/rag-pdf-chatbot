from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_and_save_vector_store


def main():
    print("Loading PDF...")
    docs = load_pdf()

    print("Splitting documents...")
    chunks = split_documents(docs)

    print("Uploading embeddings to Pinecone...")
    create_and_save_vector_store(chunks)

    print("Ingestion completed successfully!")


if __name__ == "__main__":
    main()