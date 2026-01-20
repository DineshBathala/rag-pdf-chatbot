from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

def get_qa_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
    return qa_chain
