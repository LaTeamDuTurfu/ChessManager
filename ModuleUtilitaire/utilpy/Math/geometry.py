import math
from abc import abstractmethod, ABC
from typing import Self
from PIL import Image, ImageDraw

from Console.console_utils import *


class Forme(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError("Une forme c'est abstrait, on ne peut pas en construire.")

    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def dessiner(self, image: Image, top_x: int, top_y: int):
        pass

    @abstractmethod
    def périmètre(self):
        pass

    @abstractmethod  # Ceci va forcer toutes les classes dérivées à overrider de __str__
    def __str__(self):
        pass

    def __repr__(self):  # Ceci va forcer toutes les classes dérivées à utiliser le __str__ pour représenter l'instance
        return self.__str__()


class Cercle(Forme):
    def __init__(self, rayon=1.0):
        self.__rayon = rayon

    @classmethod
    def from_rectangle(cls, rectangle: "Rectangle"):
        côté_min = min(rectangle.largeur, rectangle.longueur)
        return cls(côté_min)

    @property
    def rayon(self):
        return self.__rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def dessiner(self, image, top_x, top_y):
        pass

    def périmètre(self):
        return 2 * math.pi * self.rayon

    def __str__(self):
        return (f"Ceci est un rayon de {self.rayon}m de rayon, avec une aire de {self.aire()}m2 et un périmètre de "
                f"{self.périmètre()}m")


class Rectangle(Forme):
    # CONSTRUCTEUR
    def __init__(self, longueur: float, largeur: float):
        if longueur <= 0 or largeur <= 0:
            raise ValueError("Les dimensions du rectangles doivent être supérieure à 0.")
        self.longueur = longueur
        self.largeur = largeur

    # PROPRIÉTÉS
    @property
    def diagonale(self):
        return (self.longueur ** 2 + self.largeur ** 2) ** 0.5

    # MÉTHODES
    @property
    def aire(self):
        return self.largeur * self.longueur

    @classmethod
    def créer_rectangle_or(cls):
        nb_or = (1 + math.sqrt(5)) / 2
        return Rectangle(1, nb_or)

    @classmethod
    def créer_rect_construction(cls):
        return Rectangle(3, 4)

    @classmethod
    def from_cercle_extérieur(cls, cercle: Cercle):
        return cls(cercle.rayon * 2, cercle.rayon * 2)

    @classmethod
    def from_cercle_intérieur(cls, cercle: Cercle):
        return cls(2 * cercle.rayon * math.sin(45), 2 * cercle.rayon * math.sin(45))

    @classmethod
    def from_rectangle_rotation(cls, rectangle: Self) -> Self:
        return cls(longueur=rectangle.largeur, largeur=rectangle.longueur)

    def dessiner(self, image, top_x, top_y):
        forme: ImageDraw = ImageDraw.Draw(image)
        forme.rectangle((top_x, top_y, top_x + self.largeur, top_y + self.longueur), fill="#FF0000", outline="green")

    def périmètre(self):
        return 2 * self.largeur + 2 * self.longueur

    def obtenir_description(self):
        return (f"Rectangle de {self.largeur} de largeur et de {self.longueur} de longueur, pour une aire de "
                f"{self.aire}.")

    # OVERRIDES
    def __str__(self):
        return self.obtenir_description()


class Carré(Rectangle):
    """"""

    # VARIABLES DE CLASSE
    # aucune

    # CONSTRUCTEUR
    def __init__(self, côté: float):
        super().__init__(largeur=côté, longueur=côté)

    # MÉTHODES DE CLASSE

    # PROPRIÉTÉS

    # MÉTHODES (publiques et ensuite privées)
    def aire(self):
        pass

    def périmètre(self):
        super().périmètre()

    def obtenir_description(self):
        super().obtenir_description()

    # MÉTHODES SUPPLANTÉES / OVERRIDES
    def __str__(self):
        super().__str__()


if __name__ == '__main__':
    colored_print("Ne pas exécuter ce fichier", "red", attributs=["bold"])
