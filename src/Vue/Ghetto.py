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

        self.canvas = Canvas(self.root, width=self.width_case * dim, height=self.width_case * dim)
        self.canvas.grid(column=0, row=0)

        self.frameButton = Frame(self.root)
        self.frameButton.grid(row=0, column=1)
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
        self.labelNbRace = Label(self.frameButton, text="Nombre de race")
        self.labelNbRace.grid(column=0, row=1)
        self.nbRaceValue = IntVar(value=2)
        self.entrynbRace = Entry(self.frameButton, width=20, textvariable=self.nbRaceValue)
        self.entrynbRace.grid(column=1, row=1)

    def afficherEtape(self, listColor):
        """

        :param listColor: dict des couleurs
        :return:
        """
        for key, color in listColor.items():
            self.individus[key].graphe = self.canvas.create_rectangle(
                key[0] * self.width_case,
                key[1] * self.width_case,
                (key[0] + 1) * self.width_case,
                (key[1] + 1) * self.width_case,
                fill=color,
            )

    def launch_simu(self):
        for _ in range(self.nbRaceValue.get()):
            for case in self.individus.values():
                self.canvas.itemconfig(case.graphe, fill="red")
            time.sleep(1)
            self.canvas.update()
            for case in self.individus.values():
                self.canvas.itemconfig(case.graphe, fill="blue")
            time.sleep(1)
            self.canvas.update()
