from src.loader import load_pdf
from src.splitter import split_documents

PDF_PATH = "data/sample.pdf"   # create this folder + put 1 PDF

def main():
    documents = load_pdf(PDF_PATH)
    print(f"Loaded {len(documents)} pages")

    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("\nSample chunk:\n")
    print(chunks[0].page_content)

if __name__ == "__main__":
    main()
