import sys
from Exercices import *
from Utilitaires import *


def getChoice():
    print("\n")
    while True:
        try:
            choix = int(input(
                'Quel exercice voulez vous faire ?\n1- Eleve \n2- Maillon \n3- Liste eleves \nAutres - Quitter\n>'))
            if (choix < 0 or choix > 10):
                raise Exception('Entrez un choix valide !\n')
        except ValueError:
            print('Entrez un nombre entier !\n')
        except Exception as e:
            print(e)
        else:
            return choix


def menu() -> int:
    while True:
        choice = getChoice()
        if (choice == 1):
            studient = eleve('nom', 'prenom', 'mail', 'classe', 'moyenne_generale')
            print(studient.nom + ' ' + studient.prenom +
                  ' : \n Email : ' + studient.mail +
                  '\n Classe : ' + studient.classe +
                  '\n Moyenne generale : ' + studient.moyenne_generale)
        elif (choice == 2):
            maillon_actuel = maillon(eleve('nom', 'prenom', 'mail', 'classe', 'moyenne_generale'))
            print(str(maillon_actuel.precedent) + ' ' + str(maillon_actuel.suivant))
        elif (choice == 3):
            print(listeEleve(2002))
        else:
            return 0
    return 1
