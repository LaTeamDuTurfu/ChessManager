# Ce script sert à simuler un 'sondage' qui contient
# des questions permettant de tester vos fonctions utilitaires


# On va d'abord importer toutes les fonctions dans le module console_utils,
# ce dernier étant dans le dossier ./utilpy.Console
from utilpy.Console.console_utils import *




age = lire_entier("Quel est votre âge ? ")

age = lire_entier_positif("Quel est votre âge (nombre positif accepté) ? ")

age = lire_entier_pair("Quel est votre âge (nombre pair accepté) ?")

age = lire_entier_impair("Quel est votre âge (nombre impair accepté) ?")

age = lire_entier_intervalle("Quel est l'année de naissance du client ? ", 1900, 2023)

état_civil = lire_caractère("Quel est l'état civil du client (C, M, D, V) *** non validé *** : ")

salaire: float = lire_réel("Quel salaire horaire désirez-vous ?")

prénom = lire_chaine("Quel est le prénom du client ?")

MIN = 2
MAX = 20
mot_passe = lire_chaine_taille_intervalle(f"Veuillez saisir le nouveau mot de passe ({MIN} à {MAX} car.) ?", MIN, MAX)


état_civil = lire_caractère_selon_ensemble("Quel est l'état civil du client (C, M, D, V) *** validé *** : ", "CMDV")


veut_continuer = confirmer("Voulez-vous continuer le sondage ? ")

if not veut_continuer:
    exit()


# on confirme avec la question par défaut
if not confirmer():
    exit()


