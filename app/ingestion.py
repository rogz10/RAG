from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


def load_documents(data_dir: Path | None = None):
    """Charge les documents depuis le dossier source"""
    source_dir = data_dir or settings.data_raw_dir

    loaders = [
        DirectoryLoader(str(source_dir), glob="**/*.pdf", loader_cls=PyPDFLoader),
        DirectoryLoader(str(source_dir), glob="**/*.txt", loader_cls=TextLoader),
        DirectoryLoader(str(source_dir), glob="**/*.md", loader_cls=TextLoader),
    ]

    documents = []
    for loader in loaders:
        documents.extend(loader.load())

    return documents


def split_documents(documents):
    """Découpe les documents en morceaux exploitables par le RAG"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )

    return splitter.split_documents(documents)
