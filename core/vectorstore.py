import os
from dotenv import load_dotenv
from langchain_chroma import Chroma

load_dotenv()

def get_vectorstore(documents, embedding_model, persist_dir: str = "./chroma_db"):
    """
    Creates or loads a Chroma vectorstore. If persist_dir is empty, adds documents and persists.
    """
    os.makedirs(persist_dir, exist_ok=True)

    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model,
    )

    # Simple persistence check: if persist dir has few files, assume DB empty and add docs.
    # This avoids calling internal collection methods that may change across versions.
    files = os.listdir(persist_dir)
    if not files:
        # No persisted DB yet — add documents
        if documents:
            vectorstore.add_documents(documents)
            vectorstore.persist()

    return vectorstore
