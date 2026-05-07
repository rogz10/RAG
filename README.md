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
  requirements.txt     # dépendances Python
  README.md
```

## Rôle Des Modules

- `config.py` centralise la configuration du projet.
- `ingestion.py` gère le chargement, le nettoyage et le découpage des documents.
- `vector_store.py` gère la création des embeddings et leur stockage dans la base vectorielle.
- `rag_pipeline.py` orchestre la recherche documentaire et la génération de réponse.
- `main.py` expose les fonctionnalités principales via une API.

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
