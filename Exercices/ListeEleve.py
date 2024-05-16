from Utilitaires import *


class ListeEleve:
    def __init__(self, annee):
        self.tete = None
        self.fin = None
        self.annee = annee

    @staticmethod
    def initialiser_liste(self, annee):
        return ListeEleve(annee)

    def tailleListe(self):
        count = 0
        maillon_actuel = self.tete
        while maillon_actuel is not None:
            count += 1
            maillon_actuel = maillon_actuel.suivant
        return count

    @staticmethod
    def listeVide(self):
        return self.tete is None and self.fin is None


def listeEleve(annee):
    liste = ListeEleve(annee)
    return liste.tailleListe(), liste.listeVide()
