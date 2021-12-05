from itertools import product

from CONSTANTES import COLOR, COLOR_EMPTY
from Model.Simulation import Simulation


def launchSimu(ghetto, taille=10):
    simu = Simulation(ghetto.nbGroupeValue.get(), taille, tolerance=ghetto.toleranceValue.get())
    ghetto.afficherEtape(getListColor(simu))
    ghetto.canvas.update()
    for i in range(200):
        print(f"tour {i}")
        simu.unTour()
        ghetto.afficherEtape(getListColor(simu))
        ghetto.canvas.update()


def getListColor(simu: Simulation):
    """
    Renvoie le dict des couleurs par coordonées
    :param simu:
    :return:
    """
    colors = {}
    for (i, j) in product(range(simu.taille), range(simu.taille)):
        if (i, j) in simu.listIndividus.keys():
            colors[(i, j)] = COLOR[simu.listIndividus[(i, j)].groupe]
        else:
            colors[(i, j)] = COLOR_EMPTY
    return colors
