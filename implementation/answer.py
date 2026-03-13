from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, convert_to_messages
from langchain_core.documents import Document

from dotenv import load_dotenv


load_dotenv(override=True)

MODEL = "gpt-4.1-nano"
DB_NAME = str(Path(__file__).parent.parent / "vector_db")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Bigger net (k=5): Catch that fish + others swimming nearby with related keywords
RETRIEVAL_K = 20
vectorstore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_K})
llm = ChatOpenAI(temperature=0, model_name=MODEL)


from datetime import datetime

# "RAG-Optimized" Minimal Version (Fast & Effective)
SYSTEM_PROMPT = """You are "InsureLLM Assistant," an AI representative for Insurellm.

## RULES:
- Answer based ONLY on the provided Context
- For every statement, cite the source using [Source: filename/page]
- If information conflicts within Context, acknowledge the discrepancy
- Never speculate beyond the Context

## FORMAT:
Your response should follow this structure:
- Direct answer to the question
- Supporting details (with citations)
- Relevant disclaimers (if any)
- Next steps or suggestions (if appropriate)

## CONTEXT:
{context}

## RESPONSE:
"""


def fetch_context(question: str) -> list[Document]:
    """
    Retrieve relevant context documents for a question.
    """
    return retriever.bind(k=RETRIEVAL_K).invoke(question)


def answer_question(question: str, history: list[dict] = []) -> tuple[str, list[Document]]:
    """
    Answer the given question with RAG; return the answer and the context documents.
    """
    docs = fetch_context(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_prompt = SYSTEM_PROMPT.format(context=context)
    messages = [SystemMessage(content=system_prompt)]
    messages.extend(convert_to_messages(history))
    messages.append(HumanMessage(content=question))
    response = llm.invoke(messages)
    return response.content, docs
