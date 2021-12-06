from functools import partial
from itertools import product
from tkinter import *
from tkinter import ttk

from CONSTANTES import WIDTH_TOTAL, COLOR_EMPTY
from Controller.Simulation import launchSimu
from Vue.Individu import Individu
import time


class Ghetto:
    def __init__(self, dim=10, ):
        """:param dim: taille de la ville (longueur d'un côté)"""
        self.width_case = WIDTH_TOTAL / dim
        self.root = Tk()
        # Canvas
        self.canvas = Canvas(self.root, width=self.width_case * dim, height=self.width_case * dim)
        self.canvas.grid(column=0, row=0)

        # Frame pour les boutons
        self.frameButton = Frame(self.root)
        self.frameButton.grid(row=0, column=1)

        # Champs du nombre de groupe
        self.labelNbGroupe = Label(self.frameButton, text="Nombre de groupe")
        self.labelNbGroupe.grid(column=0, row=1)
        self.nbGroupeValue = IntVar(value=2)
        self.entrynbGroupe = Entry(self.frameButton, width=20, textvariable=self.nbGroupeValue)
        self.entrynbGroupe.grid(column=1, row=1)

        # Champs du seuil de tolérance
        self.labelTolerance = Label(self.frameButton, text="Seuil de tolérance")
        self.labelTolerance.grid(column=0, row=2)
        self.toleranceValue = IntVar(value=20)
        self.entryTolerance = Entry(self.frameButton, width=20, textvariable=self.toleranceValue)
        self.entryTolerance.grid(column=1, row=2)

        # Temps d'attente entre les tours
        self.labelTempsAttente = Label(self.frameButton, text="Temps d'attente")
        self.labelTempsAttente.grid(column=0, row=3)
        self.tempsAttenteValue = StringVar(value="0.5")
        self.entryTempsAttente = Entry(self.frameButton, width=20, textvariable=self.tempsAttenteValue)
        self.entryTempsAttente.grid(column=1, row=3)

        action = partial(launchSimu, self, dim)
        ttk.Button(self.frameButton, text="Launch Simu", command=action).grid(column=0, row=0)

        self.individus = {}
        for abscisse, ordonnee in product(range(dim), range(dim)):
            self.individus[(abscisse, ordonnee)] = Individu(abscisse, ordonnee)
            self.individus[(abscisse, ordonnee)].graphe = self.canvas.create_rectangle(
                abscisse * self.width_case,
                ordonnee * self.width_case,
                (abscisse + 1) * self.width_case,
                (ordonnee + 1) * self.width_case,
                fill=COLOR_EMPTY,
            )

    def afficherEtape(self, listColor):
        """

        :param listColor: dict des couleurs
        :return:
        """
        for key, color in listColor.items():
            self.canvas.itemconfig(self.individus[key].graphe, fill=color)

