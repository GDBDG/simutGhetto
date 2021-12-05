import logging
from itertools import product
from random import random, choice

logger = logging.getLogger()


class Individu:

    def __init__(self, groupe=0, abscisse=0, ordonnee=0):
        self.groupe = groupe
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        logger.info(f"Creation de {self}")

    def __repr__(self):
        return f"Groupe : {self.groupe}\nabscisse : {self.abscisse}, \nordonnee : {self.ordonnee}\n\n"

    def getVoisins(self, listIndividu):
        """
        Renvoie la list des individus voisins (case à côte, diagonale inclue)
        :return:
        """
        listVoisin = []
        for (abscisse, ordonnee) in product(
                range(self.abscisse - 1,  self.abscisse + 2),
                range(self.ordonnee - 1,  self.ordonnee + 2)):
            if (abscisse, ordonnee) in listIndividu.keys() and (abscisse != self.abscisse or ordonnee != self.ordonnee):
                listVoisin.append(listIndividu[(abscisse, ordonnee)])
        return listVoisin

    def getVoisinsMemeGroupe(self, listIndividu):
        """
        Renvoie les voisins de même groupe
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu) if voisin.groupe == self.groupe]

    def getVoisinsGroupeDifferent(self, listIndividu):
        """
        Renvoie les voisins de groupe différente
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu) if voisin.groupe != self.groupe]

    def estSatisfait(self, listIndividu):
        """
        Renvoie un boolean indiquant si l'individu est satisfait du nombre de ses voisins de même groupe
        Si 0 voisin : satisfait
        Si 1 ou 2 voisins : au moins 1 semblable
        Si 3, 4 ou 5 voisins : au moins 2 semblables
        Si 6, 7 ou 8 voisins : au moins 3 semblables
        :return: boolean de satisfaction
        """
        nombreVoisin = len(self.getVoisins(listIndividu))
        if not nombreVoisin:
            return True
        elif nombreVoisin <= 2:
            return len(self.getVoisinsMemeGroupe(listIndividu)) >= 1
        elif nombreVoisin <= 5:
            return len(self.getVoisinsMemeGroupe(listIndividu)) >= 2
        elif nombreVoisin <= 8:
            return len(self.getVoisinsMemeGroupe(listIndividu)) >= 3

    # def estSatisfait(self, listIndividu, taille):
    #     """
    #     Renvoie un boolean indiquant si l'individu est satisfait du nombre de ses voisins de même groupe
    #     Si 0 voisin : satisfait
    #     Si 1 ou 2 voisins : au moins 1 semblable
    #     Si 3, 4 ou 5 voisins : au moins 2 semblables
    #     Si 6, 7 ou 8 voisins : au moins 3 semblables
    #     :return: boolean de satisfaction
    #     """
    #     nombreVoisin = len(self.getVoisins(listIndividu, taille))
    #     if not nombreVoisin:
    #         return True
    #     elif nombreVoisin <= 3:
    #         return len(self.getVoisinsMemeGroupe(listIndividu, taille)) == nombreVoisin
    #     elif nombreVoisin <= 6:
    #         return len(self.getVoisinsGroupeDifferent(listIndividu, taille)) <= 1
    #     elif nombreVoisin <= 8:
    #         return len(self.getVoisinsGroupeDifferente(listIndividu, taille)) <= 2

    def demenager(self, casesLibres, listIndividus):
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
            if self.estSatisfait(listIndividus):
                break

    def unTour(self, casesLibres, listIndividus):
        """
        Va effectuer un tour de simulation pour un individu
        :param casesLibres:  liste des cases libres
        :param listIndividus: dict des individus de la simulation
        :return:
        """
        if not self.estSatisfait(listIndividus):
            self.demenager(casesLibres, listIndividus)


def getGroupeFromCompteur(compteur, nbGroupe):
    """
    Renvoie la groupe tirée aléatoirement à partir de la list des probas
    :return:
    """
    return compteur % nbGroupe
