from unittest.mock import patch

from langchain_core.documents import Document

from app.vector_store import index_documents


@patch("app.vector_store.get_vector_store")
def test_index_documents_uses_stable_ids(get_vector_store):
    document = Document(
        page_content="Contenu stable",
        metadata={"source": "document.txt"},
    )

    index_documents([document])
    first_id = get_vector_store.return_value.add_documents.call_args.kwargs["ids"][0]

    index_documents([document])
    second_id = get_vector_store.return_value.add_documents.call_args.kwargs["ids"][0]

    assert first_id == second_id
