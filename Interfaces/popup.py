from tkinter import Toplevel


class Popup:
    def __init__(self, title, geometry, root):
        self.title = title
        self.geometry = geometry
        self.root = root

    def create_popup(self):
        popup = Toplevel(self.root)  # permet de lier la popup à une fenêtre parent
        popup.title(self.title)
        popup.geometry(self.geometry)

        return popup
