import streamlit as st
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

st.title("📄 Chat with your PDF")

question = st.text_input("Ask a question about your PDF:")

if question:

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = PineconeVectorStore(
        index_name="rag-pdf-index",
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever()

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="mistral")

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    st.write(response)