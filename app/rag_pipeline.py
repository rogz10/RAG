from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from app.config import settings
from app.vector_store import get_vector_store


SYSTEM_PROMPT = """
Tu es un assistant RAG précis et fiable
Réponds uniquement avec les informations présentes dans le contexte
Si la réponse n est pas dans le contexte indique que tu ne sais pas

Contexte
{context}
"""


def build_rag_chain():
    """Construit la chaîne RAG complète"""
    llm = ChatOllama(model=settings.llm_model)
    retriever = get_vector_store().as_retriever(
        search_kwargs={"k": settings.retrieval_k},
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "{input}"),
        ],
    )

    answer_chain = prompt | llm | StrOutputParser()
    return retriever, answer_chain


def ask_question(question: str):
    """Pose une question au pipeline RAG"""
    retriever, answer_chain = build_rag_chain()
    documents = retriever.invoke(question)
    context = "\n\n".join(document.page_content for document in documents)
    answer = answer_chain.invoke(
        {
            "context": context,
            "input": question,
        },
    )

    return {
        "answer": answer,
        "sources": format_sources(documents),
    }


def format_sources(documents):
    """Prépare les sources pour la réponse API"""
    return [
        {
            "source": document.metadata.get("source"),
            "page": document.metadata.get("page"),
        }
        for document in documents
    ]
