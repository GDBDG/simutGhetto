import itertools
from unittest import mock

from src.Model.Simulation import Simulation
from src.Model.Individu import Individu


def test_getVoisin():
    # with mock.patch("typing.MutableMapping.pop"):
    simu = Simulation(1, 4)
    print(simu.listIndividus)
    expected = [individu for individu in simu.listIndividus.values() if
                (individu.abscisse <= 2) and (individu.ordonnee <= 2) and (
                        individu.abscisse != 1 or individu.ordonnee != 1)]
    assert simu.listIndividus[(1, 1)].getVoisins(simu.listIndividus, simu.taille) == expected


def test_estSatisfait():
    individu = Individu(1, 1, 1)
    # Si 1 ou 2 voisins : au moins 1 semblable
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[]):
        assert not individu.estSatisfait({})
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[1]):
        assert individu.estSatisfait({})
    # Si 3, 4 ou 5 voisins : au moins 2 semblables
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[]):
        assert not individu.estSatisfait({})
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[1, 1]):
        assert individu.estSatisfait({})
    # Si 6, 7 ou 8 voisins : au moins 3 semblables
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1, 1, 1, 1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[]):
        assert not individu.estSatisfait({})
    with mock.patch("src.Model.Individu.Individu.getVoisins", return_value=[1, 1, 1, 1, 1, 1]), \
         mock.patch("src.Model.Individu.Individu.getVoisinsMemeRace", return_value=[1, 1, 1]):
        assert individu.estSatisfait({})

def test_demenager():
    listIndividu = {(1,1): Individu(1,1,1)}
    listIndividu[(1,1)].demenager([(1,2)], listIndividu)
    assert list(listIndividu.keys()) == [(1,2)]


