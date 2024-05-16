import sys
from Exercices import *
from Utilitaires import *

def getChoice():
    print("\n")
    while True:
        try:
            choix = int(input('Quel exercice voulez vous faire ?\n1- Exercices1 \n2-  Exercices2 \n3-  Exercices3 \n4-  Exercices4 \nAutres - Quitter\n>'))
            if(choix < 0 or choix > 10):
                raise Exception('Entrez un choix valide !\n')
        except ValueError:
            print('Entrez un nombre entier !\n')
        except Exception as e:
            print(e)
        else:
            return choix

def menu() -> int :
    while True:
        choice = getChoice()
        if(choice == 1):
            jeuCartes(10)
        elif(choice == 2):
            exercice2()
        elif(choice == 3):
            exercice3()
        elif(choice == 4):
            exercice4()
        else :
            return 0
    return 1
