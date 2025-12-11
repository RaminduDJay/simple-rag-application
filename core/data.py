from langchain_core.documents import Document

# Small demo documents - replace / extend with real content or PDF loaders
documents = [
    Document(
        page_content=(
            "The T20 World Cup 2024 is in full swing, bringing excitement and drama to cricket fans worldwide. "
            "India's team, captained by Rohit Sharma, is preparing for a crucial match against Ireland, with standout "
            "player Jasprit Bumrah expected to play a pivotal role in their campaign. The tournament has already "
            "seen controversy, particularly concerning the pitch conditions at Nassau County International Cricket Stadium in New York."
        ),
        metadata={"source": "cricket news"},
    ),
    Document(
        page_content=(
            "The world of football is buzzing with excitement as major tournaments and league matches continue to captivate fans globally. "
            "In the UEFA Champions League, the semi-final matchups have been set."
        ),
        metadata={"source": "football news"},
    ),
    Document(
        page_content=(
            "The AI revolution continues to transform industries and reshape the global economy. Significant advancements in "
            "artificial intelligence have led to breakthroughs in healthcare, with AI-driven diagnostics improving patient outcomes."
        ),
        metadata={"source": "ai news"},
    ),
]
