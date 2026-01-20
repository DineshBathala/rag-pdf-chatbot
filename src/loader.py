from langchain_community.document_loaders import PyPDFLoader
import os


def load_pdf(pdf_path="data/sample.pdf"):
    """
    Loads a PDF file and returns documents.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages")

    return documents
