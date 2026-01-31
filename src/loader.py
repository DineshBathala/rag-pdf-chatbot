from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(pdf_path="data/sample.pdf"):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"Loaded {len(docs)} pages")
    return docs
