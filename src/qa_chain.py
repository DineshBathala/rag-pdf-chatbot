from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def create_qa_chain(vector_store):
    llm = ChatOllama(model="mistral")

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question based only on the following context:

        {context}

        Question: {input}
        """
    )

    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector_store.as_retriever()

    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain
