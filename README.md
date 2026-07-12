# Personal RAG

Personal RAG est une base de projet dédiée à la construction d'un assistant capable d'exploiter des documents personnels à l'aide de la génération augmentée par récupération, ou Retrieval-Augmented Generation.

L'objectif est de mettre en place une architecture claire, modulaire et extensible pour charger des documents, les indexer dans une base vectorielle, rechercher les passages pertinents et produire des réponses contextualisées avec un modèle de langage.

## Objectifs Du Projet

- Concevoir une architecture RAG propre et maintenable.
- Structurer le code autour de responsabilités séparées : ingestion, embeddings, stockage vectoriel, pipeline RAG et API.
- Expérimenter avec les outils modernes de l'écosystème LLM.
- Construire un projet présentable dans un portfolio technique.

## Fonctionnement Général

```text
Documents
  -> ingestion
  -> découpage en chunks
  -> génération d'embeddings
  -> stockage dans une base vectorielle
  -> recherche sémantique
  -> génération de réponse avec un LLM
```

Cette approche permet au modèle de répondre à partir d'un contexte documentaire précis, au lieu de s'appuyer uniquement sur ses connaissances internes.

## Stack Technique

- `Python` : langage principal du projet.
- `FastAPI` : exposition du service sous forme d'API.
- `LangChain` : orchestration des composants RAG.
- `ChromaDB` : stockage vectoriel local.
- `Hugging Face sentence-transformers` : génération des embeddings.
- `Ollama` : exécution locale de modèles de langage.
- `PyPDF` : extraction de contenu depuis des fichiers PDF.

## Fonctionnalités

- Chargement de documents depuis un dossier local.
- Support des formats PDF, TXT et Markdown.
- Découpage des documents en chunks.
- Génération d'embeddings avec `sentence-transformers`.
- Indexation locale dans `ChromaDB`.
- Réindexation idempotente sans duplication des mêmes chunks.
- Recherche sémantique sur les documents indexés.
- Génération de réponses contextualisées avec un modèle Ollama.
- API HTTP avec `FastAPI`.

## Architecture

```text
RAG/
  app/
    __init__.py
    config.py          # configuration de l'application
    ingestion.py       # chargement et préparation des documents
    main.py            # point d'entrée de l'API
    rag_pipeline.py    # orchestration du pipeline RAG
    vector_store.py    # gestion des embeddings et de la base vectorielle
  data/
    raw/               # documents sources
    processed/         # documents transformés ou nettoyés
  tests/               # tests du projet
  vector_db/           # stockage vectoriel local
  .env.example         # exemple de configuration d'environnement
  .gitignore
  pyproject.toml        # configuration des tests
  requirements.txt     # dépendances Python
  README.md
```

## Rôle Des Modules

- `config.py` centralise la configuration du projet.
- `ingestion.py` gère le chargement, le nettoyage et le découpage des documents.
- `vector_store.py` gère la création des embeddings et leur stockage dans la base vectorielle.
- `rag_pipeline.py` orchestre la recherche documentaire et la génération de réponse.
- `main.py` expose les fonctionnalités principales via une API.

## Installation

Cloner le projet puis créer un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer le fichier d'environnement :

```bash
cp .env.example .env
```

Installer Ollama puis télécharger le modèle utilisé par défaut :

```bash
brew install ollama
ollama pull llama3.2
```

## Utilisation

Ajouter les documents à interroger dans le dossier :

```text
data/raw/
```

Lancer l'API :

```bash
uvicorn app.main:app --reload
```

Vérifier que l'API fonctionne :

```bash
curl http://localhost:8000/health
```

Indexer les documents :

```bash
curl -X POST http://localhost:8000/ingest
```

Poser une question :

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Résume les documents indexés"}'
```

La documentation interactive FastAPI est disponible à l'adresse :

```text
http://localhost:8000/docs
```

## Tests

Exécuter la suite de tests :

```bash
pytest -q
```

La suite vérifie les endpoints de l'API, le chargement des documents, le découpage en chunks et la stabilité des identifiants utilisés pendant l'indexation.

## Configuration

Les variables principales sont configurées dans `.env` :

```env
APP_NAME="Personal RAG"
DATA_RAW_DIR="data/raw"
DATA_PROCESSED_DIR="data/processed"
VECTOR_DB_DIR="vector_db"
COLLECTION_NAME="personal_documents"
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL="llama3.2"
CHUNK_SIZE=1000
CHUNK_OVERLAP=150
RETRIEVAL_K=4
```

## Cas D'usage

- Interroger des documents personnels ou professionnels.
- Résumer rapidement un ensemble de fichiers.
- Retrouver des informations dans une base documentaire locale.
- Expérimenter avec les architectures RAG et les LLM open source.

## Compétences Mises En Avant

- Architecture logicielle modulaire.
- Recherche sémantique avec embeddings.
- Utilisation de bases vectorielles.
- Intégration de modèles de langage.
- Conception d'API avec Python.
- Structuration d'un projet IA exploitable dans un contexte professionnel.

## Auteur

Isidore ZONGO
