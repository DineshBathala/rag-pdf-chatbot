from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
# Using the explicit paths ensures Python finds them
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

def create_qa_chain(vector_store):
    llm = ChatOllama(model="mistral")

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question based only on the following context:

        {context}

        Question: {input}
        """
    )

    # This creates the chain that handles the LLM + Prompt
    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector_store.as_retriever()

    # This creates the final chain that connects the Retriever to the LLM
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain