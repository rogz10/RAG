import json
from pathlib import Path

import mlflow
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import InformationRetrievalEvaluator

from eval.corpus import load_eval_chunks

data_dir = Path("data/corpus_eval") # dossier contenant les documents d'évaluation
MAX_SEQ_LENGTH = 512  # longueur maximale des séquences pour le modèle de langage
#models
MODELS={
    "A":"sentence-transformers/all-MiniLM-L6-v2", # modèle de langage pour l'anglais
    "B":"sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", # modèle de langage pour le multilingue
}

# charger ensemble de questions
def load_split(name:str)->list[dict]:
    """
    charge les questions depuis le fichier JSONL correspondant à l'ensemble spécifié
    retourne une liste de dictionnaires représentant les questions
    """
    path=data_dir/f"{name}.jsonl"
    with path.open("r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f] # charger les questions depuis le fichier JSONL
    print(f"{len(rows)} questions chargées depuis {path}")
        #line = f.readline()
        # afficher quelques lignes pour vérifier le contenu du fichier
    for row in rows[:3]:
        print(row)
    return rows

def build_evaluator(rows: list[dict],corpus: dict[str,str], name:str) -> InformationRetrievalEvaluator:
    """
    construit un évaluateur d'information retrieval à partir des questions et du corpus
    retourne un objet InformationRetrievalEvaluator
    préparer l'examen : question , corpus entuer et bonnes réponses
    """
    queries={str(i): row["question"] for i, row in enumerate(rows)} # dictionnaire des questions avec l'index comme clé
    relevant_docs={str(i): [row["chunk_id"]] for i, row in enumerate(rows)} # dictionnaire id question et ensemble des bon chunks_id

    return InformationRetrievalEvaluator(
        queries=queries,
        corpus=corpus,
        relevant_docs=relevant_docs,
        name=name,
        accuracy_at_k=[1,5], # évaluer la précision à k=1,5 hit@k
        mrr_at_k=[10], # évaluer le mean reciprocal rank à k=10 mrr@k
        show_progress_bar=True, # afficher la barre de progression
    )

if __name__ == "__main__":
    chunks, _ = load_eval_chunks(data_dir)
    corpus = {chunk.metadata["chunk_id"]: chunk.page_content for chunk in chunks}
    val_rows = load_split("val")
    evaluator = build_evaluator(val_rows, corpus, "val") # construire l'évaluateur pour l'ensemble de validation
    mlflow.set_experiment("evaluate_models-rag-retrieval") # définir l'expérience mlflow
    for label,model_name in MODELS.items():
        model = SentenceTransformer(model_name) # charger le modèle de langage
        model.max_seq_length = MAX_SEQ_LENGTH # longueur maximale des séquences
        print(f"Évaluation du modèle {label} : {model_name}")
        with mlflow.start_run(run_name=f"{label}-val"):
            mlflow.log_params({ # enregistrer les paramètres de l'expérience
                "model": model_name,
                "max_seq_length": MAX_SEQ_LENGTH,
                "split": "val",
                "n_questions": len(val_rows),
                "n_corpus": len(corpus),

            })
            results = evaluator(model) # évaluer le modèle sur l'ensemble de validation
            # metriques d'évaluation
            metrics = {
                "hit_at_1": results["val_cosine_accuracy@1"], # accuracy at 1
                "hit_at_5": results["val_cosine_accuracy@5"], # accuracy at 5
                "mrr_at_10": results["val_cosine_mrr@10"], # mean reciprocal rank at 10
            }
            mlflow.log_metrics(metrics) # enregistrer les métriques d'évaluation
        print(label, {key: round(value,3) for key, value in metrics.items()}) # afficher les métriques d'évaluation

