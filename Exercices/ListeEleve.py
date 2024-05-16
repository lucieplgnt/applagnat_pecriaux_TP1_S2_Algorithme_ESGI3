import sys

from Utilitaires import *


class ListeEleve:
    def __init__(self, annee):
        self.tete = None
        self.fin = None
        self.annee = annee

    @staticmethod
    def initialiser_liste(annee):
        return ListeEleve(annee)

    def tailleListe(self):
        count = 0
        maillon_actuel = self.tete
        while maillon_actuel is not None:
            count += 1
            maillon_actuel = maillon_actuel.suivant
        return count

    def listeVide(self):
        if self.tailleListe() > 0:
            return 'liste non vide'
        else:
            return 'liste vide'


def listeEleve(annee):
    liste = ListeEleve(annee)
    return liste.listeVide() + ' : ' + str(liste.tailleListe())
