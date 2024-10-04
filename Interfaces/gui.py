# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
from CTkListbox import *


class Interface:

    def __init__(self, database):
        self.listbox: CTkListbox = None
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"../Interfaces/assets/frame0/")
        self.window = Tk()
        self.custom_font = ("Krona One", 16, "bold")
        self.database = database
        self.window.title('Chess Manager')

        # Entrys
        self.entry_1 = None
        self.entry_2 = None
        self.entry_3 = None
        self.entry_4 = None
        self.entry_5 = None
        self.entry_6 = None
        self.entry_7 = None
        self.entry_8 = None
        self.entry_9 = None
        self.entry_10 = None
        self.entry_11 = None

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def delete_selection(self):
        """ Delete la partie sélectionnée dans la database et la ListBox"""
        if self.listbox.selected is not None:
            index = self.listbox.curselection()

            # Update la Listbox
            self.listbox.delete(index)

            # Update la database
            self.database.parties.pop(index)

    def deselect_button(self):
        """Désélectionne la partie couramment sélectionnée"""
        if self.listbox.selected is not None:
            index = self.listbox.curselection()
            self.listbox.deselect(index)

    def load_database_listbox(self):
        """ Ajoute les parties dans la listbox au démarrage"""
        for game in self.database.parties:
            self.listbox.insert("end", game)

    @staticmethod
    def check_character_limit(entry_text: StringVar, max_value: int):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:max_value])

    @staticmethod
    def clear_entrys(entrys_list: list):
        """Efface les contenus des entrys"""
        for entry in entrys_list:
            entry.delete(0, "end")
        pass

    def display_info_games(self):
        """Prend les informations d'une partie et les sets dans les entry"""
        pass

    def run(self):
        self.window.geometry("1024x768")
        self.window.configure(bg="#FFFFFF")

        # Background images
        canvas = Canvas(self.window, bg="#FFFFFF", height=768, width=1024, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 0.0, 375.0, 768.0, fill="#415A77", outline="")
        canvas.create_rectangle(375.0, 0.0, 1024.0, 768.0, fill="#778DA9", outline="")

        # Listbox management
        self.listbox = CTkListbox(self.window, command=None, width=283, bg_color="#778DA9",
                                  button_color="#778DA9",
                                  fg_color="#778DA9", border_color="#1B263B", height=600, hover_color="#1B263B",
                                  label_font=self.custom_font)
        self.load_database_listbox()
        self.listbox.insert("end", "Game 1")
        self.listbox.insert("end", "Game 2")
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
        button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=self.deselect_button,
                          relief="flat")
        button_5.place(x=36.0, y=650.0, width=307.0, height=31.0)

        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(187.0, 334.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(659.0, 44.0, image=image_image_2)

        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(682.0, 149.0, image=image_image_3)

        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(622.0, 239.0, image=image_image_4)

        image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(604.0, 329.0, image=image_image_5)

        image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(579.0, 419.0, image=image_image_6)

        image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(653.0, 509.0, image=image_image_7)

        image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(640.0, 599.0, image=image_image_8)

        # Entry player Blanc
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(842.0, 44.0, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_1.place(x=754.0, y=26.0, width=176.0, height=34.0)

        # Entry player Noir
        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(842.0, 83.0, image=entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_2.place(x=754.0, y=65.0, width=176.0, height=34.0)

        # Entry jours (JJ)
        entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(779.0, 149.0, image=entry_image_3)
        entry_3_text = StringVar()  # the text in  your entry
        entry_3_text.trace("w", lambda *args: self.check_character_limit(entry_3_text, 2))
        self.entry_3 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                             textvariable=entry_3_text)
        self.entry_3.place(x=754.0, y=131.0, width=50.0, height=34.0)

        # Entry months (MM)
        entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(861.0, 149.0, image=entry_image_4)
        entry_4_text = StringVar()
        entry_4_text.trace("w", lambda *args: self.check_character_limit(entry_4_text, 2))
        self.entry_4 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                             textvariable=entry_4_text)
        self.entry_4.place(x=836.0, y=131.0, width=50.0, height=34.0)

        # Entry years (AAAA)
        entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(957.0, 149.0, image=entry_image_5)
        entry_5_text = StringVar()
        entry_5_text.trace("w", lambda *args: self.check_character_limit(entry_5_text, 4))
        self.entry_5 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                             textvariable=entry_5_text)
        self.entry_5.place(x=917.0, y=131.0, width=80.0, height=34.0)

        # Entry "Niveau Elo (White)"
        entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(814.0, 239.0, image=entry_image_6)
        self.entry_6 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_6.place(x=754.0, y=221.0, width=120.0, height=34.0)

        # Entry "Niveau Elo (Black)"
        entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        entry_bg_7 = canvas.create_image(937.0, 239.0, image=entry_image_7)
        self.entry_7 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_7.place(x=877.0, y=221.0, width=120.0, height=34.0)

        # Entry Type de Partie
        entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        entry_bg_8 = canvas.create_image(875.5, 329.0, image=entry_image_8)
        self.entry_8 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_8.place(x=754.0, y=311.0, width=243.0, height=34.0)

        # Entry durée de la partie
        entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        entry_bg_9 = canvas.create_image(819.0, 419.0, image=entry_image_9)
        self.entry_9 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_9.place(x=754.0, y=401.0, width=130.0, height=34.0)

        # Entry résultat
        entry_image_10 = PhotoImage(file=self.relative_to_assets("entry_10.png"))
        entry_bg_10 = canvas.create_image(794.0, 509.0, image=entry_image_10)
        entry_10_text = StringVar()
        entry_10_text.trace("w", lambda *args: self.check_character_limit(entry_10_text, 1))
        self.entry_10 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font,
                              textvariable=entry_10_text)
        self.entry_10.place(x=754.0, y=491.0, width=80.0, height=34.0)

        # Entry ouverture
        entry_image_11 = PhotoImage(file=self.relative_to_assets("entry_11.png"))
        entry_bg_11 = canvas.create_image(875.5, 599.0, image=entry_image_11)
        self.entry_11 = Entry(bd=0, bg="#415A77", fg="#000716", highlightthickness=0, font=self.custom_font)
        self.entry_11.place(x=754.0, y=581.0, width=243.0, height=34.0)

        canvas.create_rectangle(807.0, 146.0, 829.0, 149.0, fill="#FFFFFF", outline="")
        canvas.create_rectangle(889.0, 146.0, 911.0, 149.0, fill="#FFFFFF", outline="")

        image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(778.0, 180.0, image=image_image_9)

        image_image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        image_10 = canvas.create_image(860.0, 180.0, image=image_image_10)

        image_image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))
        image_11 = canvas.create_image(956.0, 180.0, image=image_image_11)

        image_image_12 = PhotoImage(file=self.relative_to_assets("image_12.png"))
        image_12 = canvas.create_image(941.0, 419.0, image=image_image_12)

        image_image_13 = PhotoImage(file=self.relative_to_assets("image_13.png"))
        image_13 = canvas.create_image(921.0, 518.0, image=image_image_13)

        image_image_14 = PhotoImage(file=self.relative_to_assets("image_14.png"))
        image_14 = canvas.create_image(814.0, 270.0, image=image_image_14)

        image_image_15 = PhotoImage(file=self.relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(968.0, 44.0, image=image_image_15)

        image_image_16 = PhotoImage(file=self.relative_to_assets("image_16.png"))
        image_16 = canvas.create_image(937.0, 270.0, image=image_image_16)

        image_image_17 = PhotoImage(file=self.relative_to_assets("image_17.png"))
        image_17 = canvas.create_image(969.0, 83.0, image=image_image_17)

        image_image_18 = PhotoImage(file=self.relative_to_assets("image_18.png"))
        image_18 = canvas.create_image(187.0, 319.0, image=image_image_18)

        self.window.resizable(False, False)
        self.window.mainloop()
