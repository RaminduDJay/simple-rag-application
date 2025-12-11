import os
from dotenv import load_dotenv

# LangChain Google GenAI components
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

load_dotenv()

def get_llm():
    """
    Initialize ChatGoogleGenerativeAI (Gemini).
    Make sure GOOGLE_API_KEY is set in .env
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set in environment (.env)")

    # LangChain wrapper will read GOOGLE_API_KEY; we also set it explicitly.
    os.environ["GOOGLE_API_KEY"] = api_key

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",       # change if you want another Gemini model
        temperature=0.0,
        max_output_tokens=512,
    )
    return llm

def get_embedding():
    """
    Embedding model wrapper for Gemini embeddings.
    """
    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    return embedding
