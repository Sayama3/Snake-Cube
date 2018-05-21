from Affichage import *
from Soluce import *
from validimport *
from tkinter import *
import time

snake = main()

N = 5
xdep = 1       # nombre de pièces à bouger dans l'axe x
ydep = N       # nombre de pièces à bouger dans l'axe y
zdep = N*N     # nombre de pièces à bouger dans l'axe z

  # définition du cube comme un cube 5x5x5 avec des bords remplis mais un milieu vide pour faciliter la détection des bords
haut = [-1]*N*N
milieu = [-1]*5 + [-1,0,0,0,-1]*3 + [-1]*5

  # chemin pour aller à la pièce suivante
directions = [xdep, -xdep, ydep, -ydep, zdep, -zdep]

    
if __name__ == "__main__":
    #ici tu commence la fonction pour solutionner le snake
