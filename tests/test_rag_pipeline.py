from langchain_core.documents import Document

from app.rag_pipeline import format_sources


def test_format_sources_returns_exact_passage():
    document = Document(
        page_content="passage exact utilisé pour répondre",
        metadata={
            "page": 2,
            "source": "document.pdf",
            "start_index": 120,
        },
    )

    sources = format_sources([document])

    assert sources == [
        {
            "id": 1,
            "source": "document.pdf",
            "page": 2,
            "start_index": 120,
            "passage": "passage exact utilisé pour répondre",
        },
    ]
