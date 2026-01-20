from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store


def main():
    documents = load_pdf()
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)

    print("Vector store created successfully")


if __name__ == "__main__":
    main()
