# RAG PDF Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot that allows users
to ask questions about PDF documents and receive answers based only
on the document content.

---

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique where an AI system
retrieves relevant information from external documents before generating
a response.

Instead of relying only on the model's internal knowledge, the system
first searches a vector database for relevant text chunks and then
uses those chunks as context for answering the question.  
This reduces hallucinations and improves factual accuracy.

---

## How This Project Works

1. A PDF document is loaded.
2. The text is split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. The embeddings are stored in a vector database.
5. When a user asks a question, the system retrieves the most relevant chunks.
6. The language model generates an answer using only the retrieved context.

---

## Project Structure
rag-pdf-chatbot/
│
├── app.py # Streamlit application
├── ingest.py # Loads documents and builds embeddings
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── data/ # PDF documents
├── faiss_index/ # Stored vector embeddings
│
├── src/
│ ├── loader.py # Loads PDF files
│ ├── splitter.py # Splits text into chunks
│ ├── vector_store.py # Vector database logic
│ └── qa_chain.py # Question answering pipeline

---

## How to Run the Project

Install dependencies


pip install -r requirements.txt


Run ingestion (create embeddings)


python ingest.py


Start the Streamlit app


streamlit run app.py


Open in browser


http://localhost:8501


---

## Features

- Ask questions about any PDF
- Retrieval-based answers
- FAISS vector search
- Streamlit user interface

---

## Status

✔ Core RAG pipeline completed  
✔ Document ingestion implemented  
✔ Streamlit interface working  

---

## Author

Dinesh B  
MTech CSE | AI & ML

