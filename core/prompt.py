from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt():
    """
    Simple RAG prompt that forces using the provided context.
    """
    template = """
    Answer the question using ONLY the provided context.
    If the answer is not in the context, say "I don't know" or request the user to provide more info.

    Question:
    {question}

    Context:
    {context}
    """
    prompt = ChatPromptTemplate.from_messages([("human", template)])
    return prompt
