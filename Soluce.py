"""SOLUTION DU snake PUZZLE"""
from Affichage import *
from valid import *

snake = constructionSnake()
variablePourMichel = snake #Variable que Michel à besoin pour ses fonctions
N = 5
xdep = 1       # nombre de pièces à bouger dans l'axe x
ydep = N       # nombre de pièces à bouger dans l'axe y
zdep = N*N     # nombre de pièces à bouger dans l'axe z

  # définition du cube comme un cube 5x5x5 avec des bords remplis mais un milieu vide pour faciliter la détection des bords
haut = [-1]*N*N
milieu = [-1]*5 + [-1,0,0,0,-1]*3 + [-1]*5
cube = haut + milieu*3 + haut

  # chemin pour aller à la pièce suivante
directions = [xdep, -xdep, ydep, -ydep, zdep, -zdep]

def pos(x, y, z):
    """Convertir x,y et z en position dans la liste des cubes"""
    return x+y*ydep+z*zdep

def Pcube(cube, margin=1):
    """afficher le cube"""
    for z in range(margin,N-margin):
        for y in range(margin,N-margin):
            for x in range(margin,N-margin):
                v = cube[pos(x,y,z)]
                if v == 0:
                    s = " . "
                else:
                    s = "%02d " % v
                print(s, sep="", end="")
            print()
        print()

def place(cube, position, direction, longueur, Numpiece):
    """Placer un segment dans le cube"""
    Numpiece = int()
    for _ in range(longueur):
        position += direction
        assert cube[position] == 0
        cube[position] = Numpiece
        Numpiece += 1
    return position

def unplace(cube, position, direction, longueur):
    """supprimer un segment du cube"""
    for _ in range(longueur):
        position += direction
        cube[position] = 0

def moves(position, direction, cube, Numpiece, variablePourMichel):
    """renvoyer le mouvement valide pour la position actuelle"""
    Mvalides = []
    for Ndirections in directions:
        # Impossible de continuer dans la même direction ou l'inverse de la même direction
        if Ndirections == direction or Ndirections == -direction:
            continue
        if valid(Numpiece, position, variablePourMichel, cube):
            Mvalides.append(Ndirections)
    return Mvalides

def solve(cube, position, direction, snake, Numpiece, variablePourMichel):
    """le solveur de cube"""
    if len(snake) == 0:
        print("Solution")
        Pcube(cube)
        return
    longueur, snake = snake[0], snake[1:]
    Mvalides = moves(position, direction, cube, Numpiece, variablePourMichel)
    for Ndirections in Mvalides:
        Nposition = place(position, Ndirections, longueur, Numpiece)
        solve(cube, Nposition, Ndirections, snake, Numpiece+longueur, variablePourMichel)
        unplace(cube, position, Ndirections, longueur)
        

def main(variablePourMichel, pos, xdep, snake,cube):
    # La première pièce doit être placée le long d'un bord
    position = pos(0,1,1)
    direction = xdep
    longueur = snake[0]
    position = place(cube, position, direction, longueur, 1)
    solve(cube, position, direction, snake[1:], longueur + 1, variablePourMichel)
    

if __name__ == "__main__":
    main(variablePourMichel, pos, xdep, snake,cube)
