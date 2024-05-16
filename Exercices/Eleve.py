from Utilitaires import *


class Eleve:
    def __init__(self, nom, prenom, mail, classe, moyenne_generale):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.classe = classe
        self.moyenne_generale = moyenne_generale


def eleve(nom, prenom, mail, classe, moyenne_generale):
    return Eleve(nom, prenom, mail, classe, moyenne_generale)
