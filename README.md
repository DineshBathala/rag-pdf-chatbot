# RAG PDF Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot that allows users
to ask questions about PDF documents and receive accurate answers
based strictly on the document content.

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique where an AI system
first retrieves relevant information from external documents and then
generates responses using only that retrieved content. This reduces
hallucinations and improves factual accuracy.

## How This Project Works

1. PDF documents are loaded and read.
2. Text is split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. Relevant chunks are retrieved based on user queries.
5. A language model generates answers using the retrieved text.

## Project Structure

rag-pdf-chatbot/

- app.py # Main application entry point
- requirements.txt # Project dependencies
- README.md # Project documentation
- 
├── src/
- loader.py # Loads PDF files
- splitter.py # Splits text into chunks
- vector_store.py # Stores and retrieves embeddings
- a_chain.py # Question-answering logic

