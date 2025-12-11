from langchain_core.runnables import RunnablePassthrough

def build_rag_chain(vectorstore, llm, prompt):
    """
    Build a simple RAG chain: retriever -> prompt -> llm
    Returns a runnable chain that accepts a plain question string.
    """
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 2},  # fetch top-2 relevant chunks
    )

    # chain expects a mapping with keys 'context' and 'question'
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return chain
