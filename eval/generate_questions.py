import time
from pathlib import Path
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from app.config import settings
from eval.corpus import load_eval_chunks
import json
output_path = Path("data/corpus_eval/questions.jsonl")
min_questions_length = 15  # longueur minimale des questions générées

class GeneratedQuestion(BaseModel):
    """classe pour représenter une question générée"""
    #questions:list[str]# liste de questions générées
    question_1: str
    question_2: str


    # prompt
PROMPT = """Tu prépares un examen à partir d'un document administratif français sur l'énergie.

Écris exactement deux questions en français :
- auxquelles ce passage, et lui seul, permet de répondre
- reformulées : n'emploie pas les mêmes expressions que le passage, utilise des synonymes et des tournures différentes
- compréhensibles sans voir le passage : ne dis pas « ce passage » ou « ce document ».

Passage :
{passage}"""

def generate_questions(llm, text: str) -> list[str]:
        """ demader au llm 2  questions reformulées à partir d'un passage de texte"""
        result = llm.invoke(PROMPT.format(passage=text))
        return [result.question_1, result.question_2 ]

if __name__ == "__main__":
    # charger les docs
    chunks, _ = load_eval_chunks(Path("data/corpus_eval"))
    # initialiser le llm
    llm = ChatOllama(model=settings.llm_model, temperature=0, num_predict=200).with_structured_output(GeneratedQuestion)# formulaire de sortie structurée

    seen_questions = set()# ensemble des questions déjà générées
    rejected_questions = {"llm_error": 0, "too_short": 0, "duplicate": 0} # dictionnaire des questions rejetées
    kept=0# nombre de questions conservées
    start_time = time.time()# temps de départ
    with output_path.open("w", encoding="utf-8") as f:
         for i, chunk in enumerate(chunks,start=1):
            try:
                questions = generate_questions(llm, chunk.page_content)
            except Exception as e:
                print(f"Erreur lors de la génération des questions pour le chunk {i}: {e}")
                rejected_questions["llm_error"] += 1
                continue

            for question in questions:
                question = question.strip()  # enlever les espaces
                if len(question) < min_questions_length: # si la question est trop courte, on la rejette
                    rejected_questions["too_short"] += 1
                    continue
                if question in seen_questions: # si la question est déjà vue, on la rejette
                    rejected_questions["duplicate"] += 1
                    continue

                seen_questions.add(question) #sinon on ajoute la question à l'ensemble des questions vues
                #la ligne à écrire dans le fichier de sortie
                row={
                    "question": question,
                    "chunk_id": chunk.metadata.get("chunk_id"),
                    "source": chunk.metadata.get("source"),
                    "page": chunk.metadata.get("page"),
                }
                #écrire la ligne dans le fichier de sortie
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                kept += 1 # incrémenter compteur de questions conservées

            # Afficher la progression toutes les 20 itérations
            if i % 20 == 0:
                print(f"Chunks{i}/{len(chunks)}, Temps écoulé: {time.time() - start_time:.2f}s")
    duration=time.time() - start_time
    print(f"question gardées:{kept}")
    print(f"question rejetées:{rejected_questions}")
    print(f"Temps total écoulé: {duration:.2f}s, Temps par chunk: {duration/len(chunks):.2f}s")
