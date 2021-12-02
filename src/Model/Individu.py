import logging
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

    def getVoisins(self, listIndividu):
        """
        Renvoie la list des individus voisins (case à côte, diagonale inclue)
        :return:
        """
        listVoisin = []
        for individu in listIndividu.values():
            if abs(self.abscisse - individu.abscisse) <= 1 and abs(
                    self.ordonnee - individu.ordonnee) <= 1 and individu != self:
                listVoisin.append(individu)
        return listVoisin

    def getVoisinsMemeRace(self, listIndividu):
        """
        Renvoie les voisins de même race
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu) if voisin.race == self.race]

    def getVoisinsRaceDifferente(self, listIndividu):
        """
        Renvoie les voisins de race différente
        :return:
        """
        return [voisin for voisin in self.getVoisins(listIndividu) if voisin.race != self.race]

    def estSatisfait(self, listIndividu):
        """
        Renvoie un boolean indiquant si l'individu est satisfait du nombre de ses voisins de même race
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
            return len(self.getVoisinsMemeRace(listIndividu)) >= 1
        elif nombreVoisin <= 5:
            return len(self.getVoisinsMemeRace(listIndividu)) >= 2
        elif nombreVoisin <= 8:
            return len(self.getVoisinsMemeRace(listIndividu)) >= 3

    def demenager(self, casesLibres, listIndividus):
        """
        Déplace l'individu dans une des cases libres (aléatoire), et retire l'individu de sa case initiale dans
        listIndividu
        :param casesLibres: liste des cases accessibles pour déplacer l'individu
        :param listIndividus: dictionnaire des individus de la simu (doit être le vrai et pas une copie)
        :return:
        """
        nouvelleCase = choice(casesLibres)
        for case in casesLibres:
            listIndividus.pop((self.abscisse, self.ordonnee))
            self.abscisse = nouvelleCase[0]
            self.ordonnee = nouvelleCase[1]
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

def getRaceFromProba(listProbas):
    """
    Renvoie la race tirée aléatoirement à partir de la list des probas
    :param listProbas: p[x] =sum_k=0^x p(k)
    :return:
    """
    race = 0
    proba = random()
    while proba > listProbas[race]:
        race += 1
    return race
