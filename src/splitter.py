from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_pdf

def split_documents(documents, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)


if __name__ == "__main__":
    docs = load_pdf("../data/sample.pdf")
    chunks = split_documents(docs)

    print(f"Total chunks created: {len(chunks)}")
    print("\nSample chunk:\n")
    print(chunks[0].page_content[:500])
