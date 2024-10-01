# Module contenant les fonctions utilitaires qui
# interagissent avec la console (input, print)
import os
from os import system, name
# Essayez de garder les fonctions en ordre alphabétique
# pour que ce soit plus simple pour vous et pour vous retrouver

# Au besoin, utilisez l'onglet "Structure" de PyCharm pour
# voir facilement la liste des fonctions

from termcolor import termcolor, colored  # Test salut

from ModuleUtilitaire.utilpy.Regex.regex import *

os.environ["FORCE_COLOR"] = "1"


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def colored_print(message: str, color: str = None, surlignage: str = None, attributs: list = None):  # Salut
    print(termcolor.colored(message, color, on_color=surlignage, attrs=attributs))


def color_text(text: str, color: str, attrs: list = None):
    """
    Function to return a colored and styled string.

    Args: text (str): The text to be colored. color (str): The color to apply to the text. Can be one of: 'grey',
    'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'. attrs (list): A list of style attributes. Can
    include 'bold', 'dark', 'underline', 'blink', 'reverse', 'concealed'.

    Returns:
        str: The colored and styled string.
    """
    if attrs is None:
        attrs = []
    return colored(text, color, attrs=attrs)


def confirmer(question: str = "Voulez-vous confirmer (O/N) ?") -> bool:
    """
    Demande une confirmation O/N à l'utilisateur
    :param question: si vous fournissez la question, elle doit aussi afficher les choix
                     valides (O ou N) pour indiquer à l'utilisateur ce qui est valide
    :return: vrai si l'utilisateur a confirmé (O ou o)
    """
    réponse = lire_caractère_selon_ensemble(question, "OoNn")
    if réponse.upper() == "O":
        return True
    elif réponse.upper() == "N":
        return False


def dump_dans_fichier(nom_fichier, to_dump, path_to_dump, mode="w"):
    """
    :param nom_fichier: Nom du fichier dans lequel écrire (sans le ".txt")
    :param to_dump: Objet à dump dans le fichier
    :param path_to_dump: Path du fichier dans lequel écrire
    :param mode: Mode dans lequel ouvrir le fichier (ex: "w", "a", "r", ...)
    """
    with open(f"{nom_fichier}.txt", mode) as f:
        os.chdir(path_to_dump)
        f.write(str(to_dump))


def lire_caractère(question: str) -> str:
    while True:
        saisie = input(question)
        if len(saisie) == 1 and saisie.isalpha():
            break
        colored_print("Veuillez saisir un seul caractère", "red", attributs=["bold"])

    return saisie


def lire_caractère_selon_ensemble(question: str, ensemble: str) -> str:
    """
    Comme lire_caractère, mais le caractère sera validé pour
    être certain qu'il est présent dans l'ensemble de caractères valides.
    """
    while True:
        saisie = input(question).upper()
        if len(saisie) == 1 and saisie.isalpha() and saisie in ensemble:
            break
        colored_print(f"Veuillez saisir un des caractères suivants: {ensemble}", "red", attributs=["bold"])

    return saisie


def lire_chaine(question: str) -> str:
    """
    :param question: la question à poser
    :return: valide et retourne une chaine non vide après avoir
             retiré les espaces initiaux et ceux de la fin (strip)
    """
    while True:
        chaine = input(question).strip()
        if len(chaine) > 0:
            break
        colored_print(f"Veuillez saisir une réponse non-vide.", "red", attributs=["bold"])

    return chaine


def lire_chaine_str(question: str) -> str:
    """
    :param question: la question à poser
    :return: valide et retourne une chaine non vide après avoir
             retiré les espaces initiaux et ceux de la fin (strip)
    """
    while True:
        chaine = input(question).strip()
        if len(chaine) > 0 and all([not c.isdigit() for c in chaine]):
            break
        colored_print(f"Veuillez saisir une réponse non-vide sans int ou float.", "red", attributs=["bold"])

    return chaine


def lire_chaine_taille_intervalle(question: str, taille_min: int, taille_max: int) -> str:
    """
    :param question: la question à poser
    :param taille_min: la taille minimum que doit avoir la chaine de retour
    :param taille_max: la taille maximum
    :return: une chaine avec longueur dans l'intervalle spécifié.
    """
    while True:
        chaine = input(question).strip()
        if taille_min <= len(chaine) <= taille_max:
            break
        colored_print(f"Veuillez saisir une réponse entre {taille_min} et {taille_max} caractères.", "red",
                      attributs=["bold"])

    return chaine


def lire_date(question: str):
    while True:
        date = input(question).strip()
        if format_date_valide(date):
            break
        colored_print(f"Veuillez saisir une date valide qui respecte le format DD-MM-AAAA.", "red",
                      attributs=["bold"])

    return date


def lire_entier(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            break
        except ValueError:
            colored_print("Veuillez saisir un entier seulement.", "red", attributs=["bold"])
    return entier


def lire_entier_pair(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if entier % 2 == 0:
                break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier pair.", "red", attributs=["bold"])
    return entier


def lire_entier_positif(question: str) -> int:
    while True:
        # PMC lire_entier_positif(), tu devrais réutiliser lire_entier() et valider après
        saisie = input(question)
        try:
            entier_positif = int(saisie)
            if int(entier_positif) >= 0: break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier positif.", "red", attributs=["bold"])

    return entier_positif


def lire_entier_strictement_positif(question: str) -> int:
    while True:
        # PMC lire_entier_positif(), tu devrais réutiliser lire_entier() et valider après
        saisie = input(question)
        try:
            entier_positif = int(saisie)
            if int(entier_positif) > 0: break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier supérieur à 0.", "red", attributs=["bold"])

    return entier_positif


def lire_entier_impair(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if entier % 2 != 0:
                break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier impair.", "red", attributs=["bold"])
    return entier


def lire_entier_intervalle(question: str, minimum: int, maximum: int) -> int:
    """
    Pose la question et retourne un entier validé, selon l'intervalle spécifié.

    :param question:  La question à poser
    :param minimum: La valeur minimum inclusivement
    :param maximum: Inclusivement aussi
    :return: L'entier validé selon l'intervalle.
    """
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if minimum <= entier <= maximum: break
        except ValueError:
            pass
        colored_print(f"Veuillez saisir un entier entre {minimum} et {maximum}.", "red", attributs=["bold"])
    return entier


def lire_entier_longueur_spécifique(question: str, longueur: int):
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if len(saisie) == longueur: break
        except ValueError:
            pass
        colored_print(f"Veuillez saisir un entier de longueur {longueur}.", "red", attributs=["bold"])
    return entier


def lire_entier_minimum(question: str, minimum: int) -> int:
    """
    Pose la question et retourne un entier validé, selon l'intervalle spécifié.

    :param question:  La question à poser
    :param minimum: La valeur minimum inclusivement
    :return: L'entier validé selon l'intervalle.
    """
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if minimum <= entier: break
        except ValueError:
            pass
        colored_print(f"Veuillez saisir un entier supérieur à {minimum}.", "red", attributs=["bold"])
    return entier  # test


def lire_réel(question: str) -> float:
    """
    Cette fonction s'assure que le bon séparateur décimal est utilisé
    et obtient un nombre réel validé.

    :param question:
    :return: Le nombre réel
    """
    while True:
        saisie = input(question)
        try:
            réel = float(saisie)
            break
        except ValueError:
            colored_print("Veuillez saisir un réel seulement.", "red", attributs=["bold"])

    return réel


def lire_réel_positif(question: str) -> float:
    while True:
        # PMC lire_entier_positif(), tu devrais réutiliser lire_entier() et valider après
        saisie = input(question)
        try:
            réel_positif = float(saisie)
            if float(réel_positif) >= 0: break
        except ValueError:
            pass
        colored_print("Veuillez saisir un réel positif.", "red", attributs=["bold"])

    return réel_positif


# important de mettre une garde d'importation
if __name__ == '__main__':
    print(
        "Vous ne devriez pas démarrer ce fichier directement. Utilisez le sondage pour tester vos fonctions "
        "utilitaires")
