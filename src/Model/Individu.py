import logging
from itertools import product
from random import random, choice

logger = logging.getLogger()


class Individu:

    def __init__(self, race=0, abscisse=0, ordonnee=0):
        self.race = race
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        logger.info(f"Creation de {self}")

    def __repr__(self):
        return f"Race : {self.race}\nabscisse : {self.abscisse}, \nordonnee : {self.ordonnee}\n\n"

    def getVoisins(self, listIndividu, taille):
        """
        Renvoie la list des individus voisins (case à côte, diagonale inclue)
        :return:
        """
        listVoisin = []
        for (abscisse, ordonnee) in product(
                range(max(0, self.abscisse - 1), min(taille, self.abscisse + 2)),
                range(max(0, self.ordonnee - 1), min(taille, self.ordonnee + 2))):
            if (abscisse, ordonnee) in listIndividu.keys() and (abscisse != self.abscisse or ordonnee != self.ordonnee):
                listVoisin.append(listIndividu[(abscisse, ordonnee)])
        return listVoisin

    def getVoisinsMemeRace(self, listIndividu, taille):
        """
        Renvoie les voisins de même race
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu, taille) if voisin.race == self.race]

    def getVoisinsRaceDifferente(self, listIndividu, taille):
        """
        Renvoie les voisins de race différente
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu, taille) if voisin.race != self.race]

    def estSatisfait(self, listIndividu, taille):
        """
        Renvoie un boolean indiquant si l'individu est satisfait du nombre de ses voisins de même race
        Si 0 voisin : satisfait
        Si 1 ou 2 voisins : au moins 1 semblable
        Si 3, 4 ou 5 voisins : au moins 2 semblables
        Si 6, 7 ou 8 voisins : au moins 3 semblables
        :return: boolean de satisfaction
        """
        nombreVoisin = len(self.getVoisins(listIndividu, taille))
        if not nombreVoisin:
            return True
        elif nombreVoisin <= 2:
            return len(self.getVoisinsMemeRace(listIndividu, taille)) >= 1
        elif nombreVoisin <= 5:
            return len(self.getVoisinsMemeRace(listIndividu, taille)) >= 2
        elif nombreVoisin <= 8:
            return len(self.getVoisinsMemeRace(listIndividu, taille)) >= 3

    def demenager(self, casesLibres, listIndividus, taille):
        """
        Déplace l'individu dans une des cases libres (aléatoire), et retire l'individu de sa case initiale dans
        listIndividu
        :param casesLibres: liste des cases accessibles pour déplacer l'individu
        :param listIndividus: dictionnaire des individus de la simu (doit être le vrai et pas une copie)
        :return:
        """
        for case in casesLibres:
            listIndividus.pop((self.abscisse, self.ordonnee))
            self.abscisse = case[0]
            self.ordonnee = case[1]
            listIndividus[self.abscisse, self.ordonnee] = self
            if self.estSatisfait(listIndividus, taille):
                break

    def unTour(self, casesLibres, listIndividus, taille):
        """
        Va effectuer un tour de simulation pour un individu
        :param casesLibres:  liste des cases libres
        :param listIndividus: dict des individus de la simulation
        :return:
        """
        if not self.estSatisfait(listIndividus, taille):
            self.demenager(casesLibres, listIndividus, taille)


def getRaceFromProba(compteur, nbRace):
    """
    Renvoie la race tirée aléatoirement à partir de la list des probas
    :return:
    """
    return compteur % nbRace
