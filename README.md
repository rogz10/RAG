# Personal RAG

Projet personnel de RAG pour interroger ses propres documents avec un LLM.

Ce dépôt contient pour l'instant uniquement l'architecture du projet et la documentation de départ. Les fichiers applicatifs sont volontairement vides : le code sera ajouté étape par étape.

## Objectif

Construire un assistant capable de répondre à des questions à partir de documents personnels.

Flux prévu :

```text
Documents -> ingestion -> découpage -> embeddings -> base vectorielle -> recherche -> LLM -> réponse
```

## Stack Prévue

- `Python` : langage principal.
- `FastAPI` : future API HTTP.
- `LangChain` : orchestration du pipeline RAG.
- `ChromaDB` : base vectorielle locale.
- `Hugging Face sentence-transformers` : embeddings.
- `Ollama` : exécution locale du LLM.
- `PyPDF` : lecture des fichiers PDF.

## Architecture

```text
RAG/
  app/
    __init__.py
    config.py          # configuration future
    ingestion.py       # ingestion future des documents
    main.py            # point d'entrée futur de l'API
    rag_pipeline.py    # pipeline RAG futur
    vector_store.py    # base vectorielle future
  data/
    raw/               # documents source
    processed/         # documents transformés
  tests/               # tests futurs
  vector_db/           # base vectorielle générée localement
  .env.example         # exemple de variables d'environnement
  .gitignore
  requirements.txt     # dépendances futures
  README.md
```

## Rôle Des Dossiers

- `app/` : contiendra le code principal du projet.
- `data/raw/` : contiendra les documents originaux.
- `data/processed/` : contiendra les documents préparés ou nettoyés.
- `vector_db/` : contiendra les embeddings stockés localement.
- `tests/` : contiendra les tests du projet.

## Auteur
Isidore ZONGO
