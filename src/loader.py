from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents


if __name__ == "__main__":
    docs = load_pdf("../data/sample.pdf")
    print(f"Loaded {len(docs)} pages")
