from src.vector_store import load_vector_store
from src.qa_chain import create_qa_chain

def main():
    vector_store = load_vector_store()
    qa = create_qa_chain(vector_store)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        result = qa.invoke({"input": query})
        print("\nAnswer:\n", result["answer"])

if __name__ == "__main__":
    main()
