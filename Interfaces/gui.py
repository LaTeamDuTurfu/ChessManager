# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
from CTkListbox import *
from Models import Partie


class Interface:

    def __init__(self, database):
        self.listbox: CTkListbox = None
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../Interfaces/assets/frame0/")
        self.window = Tk()
        self.custom_font = ("Krona One", 16, "bold")
        self.database = database
        self.window.title('Chess Manager')

        # Entrys (déclaration pour que python ne chiale pas)
        self.entry_player_blanc: Entry = None
        self.entry_player_noir: Entry = None
        self.entry_jours: Entry = None
        self.entry_mois: Entry = None
        self.entry_années: Entry = None
        self.entry_elo_blanc: Entry = None
        self.entry_elo_noir: Entry = None
        self.entry_type_partie: Entry = None
        self.entry_durée_partie: Entry = None
        self.entry_résultat: Entry = None
        self.entry_ouverture: Entry = None
        self.entry_moves: Entry = None

    def relative_to_assets(self, path: str) -> Path:
        """Chemin d'accès pour les assets"""
        return self.ASSETS_PATH / Path(path)

    def delete_selection(self):
        """ Delete la partie sélectionnée dans la database et la ListBox"""
        if self.listbox.selected is not None:
            index = self.listbox.curselection()

            # Update la Listbox
            self.listbox.delete(index)

            # Update la database
            self.database.parties.pop(index)

    def deselect_selection(self):
        """Désélectionne la partie couramment sélectionnée"""
        if self.listbox.selected is not None:
            # Clear le texte qui était dans les entry
            self.clear_entrys([self.entry_player_blanc, self.entry_player_noir, self.entry_jours, self.entry_mois,
                               self.entry_années, self.entry_elo_blanc, self.entry_elo_noir, self.entry_type_partie,
                               self.entry_durée_partie, self.entry_résultat, self.entry_ouverture, self.entry_moves])
            
            index = self.listbox.curselection()
            self.listbox.deselect(index)

    def load_database_listbox(self):
        """ Ajoute les parties dans la listbox au démarrage"""
        for game in self.database.parties:
            self.listbox.insert("end", game)

    @staticmethod
    def check_character_limit(entry_text: StringVar, max_value: int):
        """S'assure qu'une entry ne dépasse un certain nombre de characters"""
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:max_value])

    @staticmethod
    def clear_entrys(entrys_list: list):
        """Efface les contenus des entrys"""
        for entry in entrys_list:
            if isinstance(entry, Entry):
                entry.delete(0, "end")
            elif isinstance(entry, Text):
                entry.delete("1.0", "end")

    def display_info_games(self, game_info=None):
        """Prend les informations d'une partie et les sets dans les entry"""
        # Clear le texte qui était dans les entry
        self.clear_entrys([self.entry_player_blanc, self.entry_player_noir, self.entry_jours, self.entry_mois,
                           self.entry_années, self.entry_elo_blanc, self.entry_elo_noir, self.entry_type_partie,
                           self.entry_durée_partie, self.entry_résultat, self.entry_ouverture, self.entry_moves])

        # Va get l'index sélectionné
        index = self.listbox.curselection()

        # Trouve la partie dans la database
        selected_game: Partie = self.database.parties[index]

        # Fill les entry avec les game infos
        self.entry_player_blanc.insert(0, selected_game.joueur1.nom)
        self.entry_player_noir.insert(0, selected_game.joueur2.nom)
        self.entry_jours.insert(0, selected_game.date[0])
        self.entry_mois.insert(0, selected_game.date[1])
        self.entry_années.insert(0, selected_game.date[2])
        self.entry_elo_blanc.insert(0, selected_game.joueur1.elo)
        self.entry_elo_noir.insert(0, selected_game.joueur2.elo)
        self.entry_type_partie.insert(0, selected_game.type_partie)
        self.entry_durée_partie.insert(0, selected_game.durée)
        self.entry_résultat.insert(0, selected_game.résultat)
        self.entry_ouverture.insert(0, selected_game.ouverture)
        self.entry_moves.insert("1.0", selected_game.moves)

    def run_main_window(self):
        """Lance la mainloop de l'interface/Catalogue"""
        self.window.geometry("1024x768")
        self.window.configure(bg="#FFFFFF")

        # Background images
        canvas = Canvas(self.window, bg="#FFFFFF", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 0.0, 375.0, 768.0, fill="#415A77", outline="")
        canvas.create_rectangle(375.0, 0.0, 1024.0, 768.0, fill="#778DA9", outline="")

        # Listbox management
        self.listbox = CTkListbox(self.window, command=self.display_info_games, width=283, bg_color="#778DA9",
                                  button_color="#778DA9",
                                  fg_color="#778DA9", border_color="#1B263B", height=600, hover_color="#1B263B",
                                  label_font=self.custom_font)
        self.load_database_listbox()
        self.listbox.place(x=32, y=26)

        # Button "Add"
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_1 clicked"), relief="flat")
        button_1.place(x=435.0, y=673.0, width=220.0, height=58.0)

        # Button "Save"
        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_2 clicked"),
                          relief="flat")
        button_2.place(x=676.923095703125, y=673.0, width=218.076904296875, height=58.0)

        # Button "Moves"
        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_3 clicked"),
                          relief="flat")
        button_3.place(x=934.0, y=673.0, width=54.0, height=58.0)

        # Button "Delete"
        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=self.delete_selection,
                          relief="flat")
        button_4.place(x=36.0, y=691.0, width=306.98345947265625, height=58.0)

        # Button "Deselect"
        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=self.deselect_selection,
                          relief="flat")
        button_5.place(x=36.0, y=650.0, width=307.0, height=31.0)

        # Entry player Blanc
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(842.0, 44.0, image=entry_image_1)
        self.entry_player_blanc = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_player_blanc.place(x=754.0, y=26.0, width=176.0, height=34.0)

        # Entry player Noir
        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(842.0, 83.0, image=entry_image_2)
        self.entry_player_noir = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_player_noir.place(x=754.0, y=65.0, width=176.0, height=34.0)

        # Entry jours (JJ)
        entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(779.0, 149.0, image=entry_image_3)
        entry_3_text = StringVar()  # the text in  your entry
        entry_3_text.trace("w", lambda *args: self.check_character_limit(entry_3_text, 2))
        self.entry_jours = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                                 textvariable=entry_3_text)
        self.entry_jours.place(x=754.0, y=131.0, width=50.0, height=34.0)

        # Entry months (MM)
        entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(861.0, 149.0, image=entry_image_4)
        entry_4_text = StringVar()
        entry_4_text.trace("w", lambda *args: self.check_character_limit(entry_4_text, 2))
        self.entry_mois = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                                textvariable=entry_4_text)
        self.entry_mois.place(x=836.0, y=131.0, width=50.0, height=34.0)

        # Entry years (AAAA)
        entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(957.0, 149.0, image=entry_image_5)
        entry_5_text = StringVar()
        entry_5_text.trace("w", lambda *args: self.check_character_limit(entry_5_text, 4))
        self.entry_années = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                                  textvariable=entry_5_text)
        self.entry_années.place(x=917.0, y=131.0, width=80.0, height=34.0)

        # Entry "Niveau Elo (White)"
        entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(814.0, 239.0, image=entry_image_6)
        self.entry_elo_blanc = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_elo_blanc.place(x=754.0, y=221.0, width=120.0, height=34.0)

        # Entry "Niveau Elo (Black)"
        entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        entry_bg_7 = canvas.create_image(937.0, 239.0, image=entry_image_7)
        self.entry_elo_noir = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_elo_noir.place(x=877.0, y=221.0, width=120.0, height=34.0)

        # Entry Type de Partie
        entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        entry_bg_8 = canvas.create_image(875.5, 300.0, image=entry_image_8)
        self.entry_type_partie = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_type_partie.place(x=754.0, y=282.0, width=243.0, height=34.0)

        # Entry durée de la partie
        entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        entry_bg_9 = canvas.create_image(819.0, 361.0, image=entry_image_9)
        self.entry_durée_partie = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_durée_partie.place(x=754.0, y=343.0, width=130.0, height=34.0)

        # Entry résultat
        entry_image_10 = PhotoImage(file=self.relative_to_assets("entry_10.png"))
        entry_bg_10 = canvas.create_image(794.0, 422.0, image=entry_image_10)
        entry_10_text = StringVar()
        entry_10_text.trace("w", lambda *args: self.check_character_limit(entry_10_text, 1))
        self.entry_résultat = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                                    textvariable=entry_10_text)
        self.entry_résultat.place(x=754.0, y=404.0, width=80.0, height=34.0)

        # Entry ouverture
        entry_image_11 = PhotoImage(file=self.relative_to_assets("entry_11.png"))
        entry_bg_11 = canvas.create_image(875.5, 483.0, image=entry_image_11)
        self.entry_ouverture = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_ouverture.place(x=754.0, y=465.0, width=243.0, height=34.0)

        # Entry moves
        entry_image_12 = PhotoImage(file=self.relative_to_assets("entry_12.png"))
        entry_bg_12 = canvas.create_image(875.5, 582.5, image=entry_image_12)
        self.entry_moves = Text(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_moves.place(x=754.0, y=526.0, width=243.0, height=111.0)

        canvas.create_rectangle(807.0, 146.0, 829.0, 149.0, fill="#FFFFFF", outline="")
        canvas.create_rectangle(889.0, 146.0, 911.0, 149.0, fill="#FFFFFF", outline="")

        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(187.0, 334.0, image=image_image_1)

        # Texte joueur
        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(659.0, 44.0, image=image_image_2)

        # Texte Date
        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(682.0, 149.0, image=image_image_3)

        # Texte Niveau (Elo)
        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(622.0, 239.0, image=image_image_4)

        # Texte type de partie
        image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(604.0, 300.0, image=image_image_5)

        # Texte Durée de la partie
        image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(579.0, 361.0, image=image_image_6)

        # Texte Résultat
        image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(653.0, 422.0, image=image_image_7)

        # Texte Ouverture
        image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(640.0, 483.0, image=image_image_8)

        # Texte Moves
        image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(668.0, 544.0, image=image_image_9)

        # Texte JJ
        image_image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        image_10 = canvas.create_image(778.0, 180.0, image=image_image_10)

        # Texte MM
        image_image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))
        image_11 = canvas.create_image(860.0, 180.0, image=image_image_11)

        # Texte AAAA
        image_image_12 = PhotoImage(file=self.relative_to_assets("image_12.png"))
        image_12 = canvas.create_image(956.0, 180.0, image=image_image_12)

        # Texte minutes
        image_image_13 = PhotoImage(file=self.relative_to_assets("image_13.png"))
        image_13 = canvas.create_image(941.0, 361.0, image=image_image_13)

        # Texte Blanc/Noir/Draw
        image_image_14 = PhotoImage(file=self.relative_to_assets("image_14.png"))
        image_14 = canvas.create_image(921.0, 422.0, image=image_image_14)

        # Texte Blanc
        image_image_15 = PhotoImage(file=self.relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(814.0, 270.0, image=image_image_15)

        # Texte Blanc
        image_image_16 = PhotoImage(file=self.relative_to_assets("image_16.png"))
        image_16 = canvas.create_image(968.0, 44.0, image=image_image_16)

        # Texte Noir
        image_image_17 = PhotoImage(file=self.relative_to_assets("image_17.png"))
        image_17 = canvas.create_image(937.0, 270.0, image=image_image_17)

        # Texte Noir
        image_image_18 = PhotoImage(file=self.relative_to_assets("image_18.png"))
        image_18 = canvas.create_image(969.0, 83.0, image=image_image_18)

        # Texte placeholder
        image_image_19 = PhotoImage(file=self.relative_to_assets("image_19.png"))
        image_19 = canvas.create_image(187.0, 319.0, image=image_image_19)

        self.window.resizable(False, False)
        self.window.mainloop()
