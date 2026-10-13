from app.ontologie import CLASSES, RELATIONS, verifier_triplet


def test_relations_utilisent_des_classes_connues():

    for relation, (depart, arrivee) in RELATIONS.items():
        assert depart in CLASSES
        assert arrivee in CLASSES
def test_verifier_triplet_valide():
    # Test d'un triplet valide
     resultat= verifier_triplet("Centrale", "SITUEE_A", "Territoire")
     assert resultat == []

def test_mauvais_depart():
    # Test d'un triplet avec un mauvais départ
    resultat= verifier_triplet("Centrale", "FILIALE_DE", "Societe")
    assert (len(resultat)) ==1
def test_mauvaise_relation():
    resultat= verifier_triplet("Societe", "GERE", "Centrale")
    assert(len(resultat)) == 1
