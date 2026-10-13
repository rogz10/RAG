
# set classes ontologie du graphe
CLASSES={ "Territoire", "Centrale","Unite","Societe","Projet", "Combustible","Texte"}

# dictionnaire des relations entre les classes(Relation-> (depart-> arrivee))
RELATIONS={
    "SITUEE_A":("Centrale","Territoire"),
    "EXPLOITE":("Societe","Centrale"),
    "FILIALE_DE":("Societe","Societe"),
    "COMPREND":("Centrale","Unite"),
    "PARTAGE_INFRA_AVEC":("Centrale","Centrale"),
    "UTILISE":("Centrale","Combustible"),
    "CONVERTIE_A":("Centrale","Combustible"),
    "PORTE":("Societe","Projet"),
    "CITE":("Texte","Texte"),
    "ABROGE":("Texte","Texte"),
    "CONCERNE":("Texte","Territoire"),

}

def verifier_triplet(classe_depart, relation, classe_arrivee):
    """
    Vérifie si le triplet (classe_depart, relation, classe_arrivee) est valide
    retourne une liste d'erreurs si le triplet est invalide, sinon retourne une liste vide.
    """
    erreur=[]
    if relation not in RELATIONS:
        erreur.append(f"Relation '{relation}' inconnue.")
        return erreur

    depart_attendu, arrivee_attendu = RELATIONS[relation]
    if classe_depart != depart_attendu:
        erreur.append(f"La classe de départ '{classe_depart}' ne correspond pas à la relation '{relation}'.")
    if classe_arrivee != arrivee_attendu:
        erreur.append(f"La classe d'arrivée '{classe_arrivee}' ne correspond pas à la relation '{relation}'.")
    return erreur

if __name__ == "__main__":
    print(verifier_triplet("Centrale", "SITUEE_A", "Territoire"))
    print(verifier_triplet("Centrale", "FILIALE_DE", "Societe"))
    print(verifier_triplet("Societe", "GERE", "Centrale"))
