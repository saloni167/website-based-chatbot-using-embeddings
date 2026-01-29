from langchain_openai import ChatOpenAI

SYSTEM_RULES = """
You answer questions strictly using the supplied context.
Do not use outside knowledge.
If the answer is missing, reply exactly:
"The answer is not available on the provided website."
"""

def answer_question(question: str, vector_db):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    # documents = retriever.get_relevant_documents(question)
    documents = retriever.invoke(question)


    if not documents:
        return "The answer is not available on the provided website."

    context = "\n".join(doc.page_content for doc in documents)

    llm = ChatOpenAI(temperature=0)

    messages = [
        {"role": "system", "content": SYSTEM_RULES},
        {"role": "user", "content": f"Context:\n{context}"},
        {"role": "user", "content": f"Question:\n{question}"}
    ]

    response = llm.invoke(messages).content
    return response
