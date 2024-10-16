from Models import *
import os


class Database:
    def __init__(self):
        self.parties: list = []
        self.folder_path = './Data'

    def load_parties(self):
        for file in os.listdir(self.folder_path): # Pour parcourir tous les fichiers des dossiers
            if file.endswith('.pgn'):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r') as f:
                    # Initialise le joueur 1
                    joueur1 = self.strip_and_initialize_player(f.readline())

                    # Initialise le joueur 2
                    joueur2 = self.strip_and_initialize_player(f.readline())

                    # Lit et sépare la date
                    date = f.readline()
                    date = date.strip().strip('"')
                    date = date.split("-")

                    # Lit et strip le non-nécessaire
                    type_partie = self.strip_brackets_quotes(f.readline())

                    # Lit et strip le non-nécessaire
                    durée = self.strip_brackets_quotes(f.readline())

                    # Lit et strip le non-nécessaire
                    résultat = self.strip_brackets_quotes(f.readline())

                    # Lit et strip le non-nécessaire
                    ouverture = self.strip_brackets_quotes(f.readline())

                    moves = f.readline()

                    # Instancie et ajouter la partie à la database
                    nouvelle_partie = Partie(joueur1, joueur2, date, type_partie, durée, résultat, ouverture, moves)
                    self.parties.append(nouvelle_partie)

        print('Les parties ont été téléchargées avec succès. ✅')

    def save_partie(self, filename, game: Partie):
        file_path = os.path.join(self.folder_path, f"{filename}.pgn")

        with open(file_path, 'a') as f:
            f.write(f'["{game.joueur1.nom}", {game.joueur1.elo}]\n')
            f.write(f'["{game.joueur2.nom}", {game.joueur2.elo}]\n')
            f.write(f'"{game.date[0]}-{game.date[1]}-{game.date[2]}"\n')
            f.write(f'["{game.type_partie}"]\n')
            f.write(f'["{game.durée}"]\n')
            f.write(f'["{game.résultat}"]\n')
            f.write(f'["{game.ouverture}"]\n')
            f.write(game.moves)

        print(f'Le fichier {filename} a été sauvegardé dans {self.folder_path}')

    def delete_file(self, filename):
        os.remove(f"{self.folder_path}/{filename}.pgn")

    @staticmethod
    def strip_brackets_quotes(string):
        return string.strip().strip("[]").strip('"')

    @staticmethod
    def strip_and_initialize_player(string):
        string = string.strip().strip("[]").rsplit(',', 1)
        return Joueur(string[0].strip().strip('"'), int(string[1].strip()))
