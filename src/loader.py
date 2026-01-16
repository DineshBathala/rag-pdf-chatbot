from langchain.document_loaders import PyPDFLoader

def load_pdf(pdf_path: str):
    """
    Loads a PDF file and returns documents.
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents
