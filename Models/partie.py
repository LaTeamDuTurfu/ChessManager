from Models.joueur import Joueur


class Partie:
    def __init__(self, joueur1, joueur2, date, type_partie, durée, résultat, ouverture, moves):
        self.joueur1: Joueur = joueur1
        self.joueur2: Joueur = joueur2
        self.date = date  # Format DD/MM/AAAA
        self.type_partie: str = type_partie
        self.durée: int = durée  # Durée en minutes
        self.résultat = résultat
        self.ouverture: str = ouverture
        self.moves: str = moves

    def __str__(self):
        return f"{self.joueur1} vs {self.joueur2} | {self.type_partie} | {self.date}"

    def __repr__(self):
        self.__str__()



