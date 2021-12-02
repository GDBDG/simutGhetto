from CONSTANTES import COLOR_EMPTY


class Individu:
    def __init__(self, abscisse=0, ordonnee=0, color=COLOR_EMPTY):
        """
        :param abscisse: abscisse de la case dans la ville
        :param ordonnee: ordonnée de la case dans la ville
        :param color: couleur du rectangle représentant la case
        """
        self.graphe = None
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
