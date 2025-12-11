import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# load .env
load_dotenv()

from core.llm import get_llm, get_embedding
from core.data import documents
from core.prompt import get_rag_prompt
from core.vectorstore import get_vectorstore
from rag.simple_rag_chain import build_rag_chain
from utils.logger import logger

# Simple Pydantic model here as well (or import from models/entity.py)
class ChatReq(BaseModel):
    question: str

app = FastAPI(title="RAG Chatbot", version="1.0")

logger.info("Starting RAG Chatbot app")

# Initialize components
llm = get_llm()
logger.info("LLM initialized")

embedding_model = get_embedding()
logger.info("Embedding model initialized")

vectorstore = get_vectorstore(documents, embedding_model)
logger.info("Vectorstore initialized")

prompt = get_rag_prompt()
logger.info("Prompt template ready")

rag_chain = build_rag_chain(vectorstore, llm, prompt)
logger.info("RAG chain built")

@app.get("/")
async def root():
    return {"status": "success", "message": "RAG Chatbot running"}

@app.post("/api/simple_rag")
async def simple_rag(req: ChatReq):
    try:
        logger.info(f"Received question: {req.question}")
        response = rag_chain.invoke(req.question)
        # response may be an object with .content
        content = getattr(response, "content", str(response))
        logger.info(f"Answer: {content}")
        return {"status": "success", "response": content}
    except Exception as e:
        logger.exception("RAG error")
        return {"status": "fail", "response": str(e)}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
