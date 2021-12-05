from copy import deepcopy
from itertools import product

from CONSTANTES import FACTEUR_VIDE
from Model.Individu import Individu, getGroupeFromCompteur
from random import random, choice, shuffle


class Simulation:
    def __init__(self, nbGroupe, taille=10):
        """
        Crée une grille d'individus, et supprime ceux des 4 coins,
        ainsi que 10 % des individus
        :param taille:
        """
        self.listIndividus = {}
        self.taille = taille
        for abscisse, ordonnee in product(range(taille), range(taille)):
            self.listIndividus[(abscisse, ordonnee)] = Individu(getGroupeFromCompteur(abscisse + ordonnee, nbGroupe), abscisse, ordonnee)
        for _ in range(taille * taille // FACTEUR_VIDE):
            self.listIndividus.pop(choice(list(self.listIndividus.keys())))

    def getCasesLibres(self):
        """
        Renvoie la liste des cases dans les quelles il n'y a pas d'individu
        :return:
        """
        return [(i, j) for (i, j) in product(range(self.taille), range(self.taille)) if
                (i, j) not in self.listIndividus.keys()]

    def unTour(self):
        """
        Fait un tour de simulation
        Regarde tous les individus, et les déplace dans une case libre si dispo
        :return:
        """
        casesLibres = self.getCasesLibres()
        shuffle(casesLibres)
        for individu in deepcopy(self.listIndividus).values():
            coord = (individu.abscisse, individu.ordonnee)
            individu.unTour(casesLibres, self.listIndividus, self.taille)
            casesLibres.append(coord)
            casesLibres.remove((individu.abscisse, individu.ordonnee))
