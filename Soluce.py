"""SOLUTION DU snake PUZZLE"""
from Iannis import *

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

def pos(x, y, z):
    """Convertir x,y et z en position dans la liste des cubes"""
    return x+y*ydep+z*zdep

def Pcube(losange, margin=1):
    """afficher le cube"""
    for z in range(margin,N-margin):
        for y in range(margin,N-margin):
            for x in range(margin,N-margin):
                v = losange[pos(x,y,z)]
                if v == 0:
                    s = " . "
                else:
                    s = "%02d " % v
                print(s, sep="", end="")
            print()
        print()

def place(losange, position, direction, longueur, Numpiece):
    """Placer un segment dans le cube"""
    for _ in range(longueur):
        position += direction
        assert losange[position] == 0
        losange[position] = Numpiece
        Numpiece += 1
    return position

def unplace(losange, position, direction, longueur):
    """supprimer un segment du cube"""
    for _ in range(longueur):
        position += direction
        losange[position] = 0

def valid(losange, position, direction, longueur):
    """renvoyer vrai si un mouvement est valide"""
    for _ in range(longueur):
        position += direction
        if losange[position] != 0:
            return False
    return True

def moves(losange, position, direction, longueur):
    """renvoyer le mouvement valide pour la position actuelle"""
    Mvalides = []
    for Ndirections in directions:
        # Impossible de continuer dans la même direction ou l'inverse de la même direction
        if Ndirections == direction or Ndirections == -direction:
            continue
        if valid(losange, position, Ndirections, longueur):
            Mvalides.append(Ndirections)
    return Mvalides

from Iannis import *
def solve(losange, position, direction, snake, Numpiece):
    """le solveur de cube"""
    import time
    if len(snake) == 0:
        print("Solution")
        Pcube(losange)
        return
    longueur, snake = snake[0], snake[1:]
    Mvalides = moves(losange, position, direction, longueur)
    for Ndirections in Mvalides:
        Nposition = place(losange, position, Ndirections, longueur, Numpiece)
        solve(losange, Nposition, Ndirections, snake, Numpiece+longueur)
        unplace(losange, position, Ndirections, longueur)
        
        print(Nposition, time.sleep(0.3))
        

def main():
    # La première pièce doit être placée le long d'un bord
    position = pos(0,1,1)
    direction = xdep
    longueur = snake[0]
    position = place(losange, position, direction, longueur, 1)
    solve(losange, position, direction, snake[1:], longueur + 1)

if __name__ == "__main__":
    main()
