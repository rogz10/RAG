import os
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def _get_path(name: str, default: Path) -> Path:
    """Retourne un chemin depuis une variable d environnement ou une valeur par défaut"""
    value = os.getenv(name)
    if not value:
        return default

    # Si le chemin est relatif on le rattache à la racine du projet
    path = Path(value)
    return path if path.is_absolute() else BASE_DIR / path


@dataclass(frozen=True)
class Settings:
    """Configuration centrale de l application RAG"""

    # Nom affiché par l application ou l API
    app_name: str = os.getenv("APP_NAME", "Personal RAG")

    # Dossiers principaux utilisés pendant le traitement des documents
    data_raw_dir: Path = _get_path("DATA_RAW_DIR", BASE_DIR / "data" / "raw")
    data_processed_dir: Path = _get_path(
        "DATA_PROCESSED_DIR",
        BASE_DIR / "data" / "processed",
    )
    vector_db_dir: Path = _get_path("VECTOR_DB_DIR", BASE_DIR / "vector_db")

    # Paramètres liés à la base vectorielle et aux modèles IA
    collection_name: str = os.getenv("COLLECTION_NAME", "personal_documents")
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2",
    )
    llm_model: str = os.getenv("LLM_MODEL", "llama3.2")

    # Paramètres du découpage documentaire et de la recherche sémantique
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "150"))
    retrieval_k: int = int(os.getenv("RETRIEVAL_K", "4"))


# Instance partagée à importer dans les autres modules
settings = Settings()
