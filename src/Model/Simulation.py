from copy import deepcopy
from itertools import product

from Model.Individu import Individu, getRaceFromProba
from random import random, choice


class Simulation:
    def __init__(self, nbRace, taille=10):
        """
        Crée une grille d'individus, et supprime ceux des 4 coins,
        ainsi que 10 % des individus
        :param taille:
        :param listProbaRace: p[x] =sum_k=0^x p(k)
        """
        self.listIndividus = {}
        self.taille = taille
        for abscisse, ordonnee in product(range(taille), range(taille)):
            condition1 = (abscisse + ordonnee)
            condition2 = not (abscisse == taille - 1 and not ordonnee)
            condition3 = not (ordonnee == taille - 1 and not abscisse)
            condition4 = not (ordonnee == taille - 1 and abscisse == taille - 1)
            if condition1 and condition2 and condition3 and condition4:
                self.listIndividus[(abscisse, ordonnee)] = Individu(getRaceFromProba(abscisse + ordonnee, nbRace), abscisse, ordonnee)
        # Retirer 10 % des individus
        for _ in range(taille*taille//10):
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
        for individu in deepcopy(self.listIndividus).values():
            individu.unTour(self.getCasesLibres(), self.listIndividus, self.taille)
