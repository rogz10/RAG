



def letter_proportion(text:str) -> float:
    """
    calcule la proportion de lettres dans un texte et
    retourne la proportion de lettres dans le texte
    """
    if not text:
        return 0.0

    total_chars = len(text)
    letter_count = sum(1 for char in text if char.isalpha())

    return letter_count / total_chars

def usable_chunk(text:str,min_caracters:int=200,min_letters:float=0.5):
    """
    Vérifie si un chunk de texte est exploitable en fonction de sa longueur et de la proportion de lettres
    retourne True si le chunk est utilisable, False sinon
    """
    return len(text) >= min_caracters and letter_proportion(text) >= min_letters
