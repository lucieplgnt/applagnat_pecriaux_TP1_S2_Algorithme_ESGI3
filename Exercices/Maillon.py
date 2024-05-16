from Utilitaires import *


class Maillon:
    def __init__(self, eleve):
        self.eleve = eleve
        self.suivant = None
        self.precedent = None

    @staticmethod
    def creerMaillon(eleve):
        return Maillon(eleve)


def maillon(eleve):
    return Maillon(eleve)
