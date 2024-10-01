from Models import *
import os


class Database:
    def __init__(self):
        self.parties = []
        self.folder_path = '../Data'

    def load_parties(self):
        for file in os.listdir(self.folder_path): # Pour parcourir tous les fichiers du dossiers
            if file.endswith('.pgn'):
                file_path = os.path.join(self.folder_path, file)

                with open(file_path, 'r') as f:
                    joueur1 = f.readline()
                    joueur2 = f.readline()
                    date = f.readline()
                    type_partie = f.readline()
                    durée = f.readline()
                    résultat = f.readline()
                    ouverture = f.readline()
                    moves = f.readline()
                    nouvelle_partie = Partie(joueur1, joueur2, date, type_partie, durée, résultat, ouverture, moves)
                    self.parties.append(nouvelle_partie)

        print('Les parties ont été téléchargées avec succès.')

    def save_partie(self, filename, partie):
        file_path = os.path.join(self.folder_path, filename)

        with open(file_path, 'a') as f:
            f.write(partie.joueur1)
            f.write(partie.joueur2)
            f.write(partie.date)
            f.write(partie.type_partie)
            f.write(partie.durée)
            f.write(partie.résultat)
            f.write(partie.ouverture)
            f.write(partie.moves)

        print(f'Le fichier {filename} a été sauvegardé dans {self.folder_path}')


