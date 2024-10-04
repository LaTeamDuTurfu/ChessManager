from Models import *
import os


class Database:
    def __init__(self):
        self.parties: list = []
        self.folder_path = './Data'

    def load_parties(self):
        for file in os.listdir(self.folder_path): # Pour parcourir tous les fichiers du dossiers
            if file.endswith('.pgn'):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r') as f:
                    joueur1 = f.readline().strip()
                    joueur1 = joueur1.strip("[]")
                    joueur1 = joueur1.rsplit(',', 1)
                    joueur1 = Joueur(joueur1[0].strip().strip('"'), int(joueur1[1].strip()))
                    joueur2 = f.readline().strip()
                    joueur2 = joueur2.strip("[]")
                    joueur2 = joueur2.rsplit(',', 1)
                    joueur2 = Joueur(joueur2[0].strip().strip('"'), int(joueur2[1].strip()))
                    date = f.readline()
                    type_partie = f.readline()
                    durée = f.readline()
                    résultat = f.readline()
                    ouverture = f.readline()
                    moves = f.readline()
                    nouvelle_partie = Partie(joueur1, joueur2, date, type_partie, durée, résultat, ouverture, moves)
                    self.parties.append(nouvelle_partie)

        print('Les parties ont été téléchargées avec succès.')

    def save_partie(self, filename, game: Partie):
        file_path = os.path.join(self.folder_path, filename)

        with open(file_path, 'a') as f:
            f.write(f'["{game.joueur1.nom}", {game.joueur1.niveau}]')
            f.write(f'["{game.joueur2.nom}", {game.joueur2.niveau}]')
            f.write(game.date)
            f.write(game.type_partie)
            f.write(game.durée)
            f.write(game.résultat)
            f.write(game.ouverture)
            f.write(game.moves)

        print(f'Le fichier {filename} a été sauvegardé dans {self.folder_path}')


