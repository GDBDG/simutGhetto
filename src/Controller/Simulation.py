from itertools import product

from CONSTANTES import COLOR, COLOR_EMPTY
from Model.Simulation import Simulation


def launchSimu(ghetto, taille=10):
    simu = Simulation(2, taille)

    for i in range(200):
        print(f"tour {i}")
        ghetto.afficherEtape(getListColor(simu))
        ghetto.canvas.update()
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
            colors[(i, j)] = COLOR[simu.listIndividus[(i, j)].race]
        else:
            colors[(i, j)] = COLOR_EMPTY
    return colors

