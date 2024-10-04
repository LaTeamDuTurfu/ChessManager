class Joueur:
    def __init__(self, nom, niveau):
        self.nom: str = nom
        self.elo: int = niveau

    def __repr__(self):
        return f'{self.nom} - {self.elo}'
