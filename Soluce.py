"""SOLUTION DU snake PUZZLE"""
from Affichage import *
from valid import *

snake = constructionSnake()
assert sum(snake) == 27 #vérifier que la liste comporte au total 27 cubes

N = 5
xdep = 1       # nombre de pièces à bouger dans l'axe x
ydep = N       # nombre de pièces à bouger dans l'axe y
zdep = N*N     # nombre de pièces à bouger dans l'axe z
empty = 0

  # définition du cube comme un cube 5x5x5 avec des bords remplis mais un milieu vide pour faciliter la détection des bords
haut = [-1]*N*N
milieu = [-1]*5 + [-1,0,0,0,-1]*3 + [-1]*5
cube = haut + milieu*3 + haut

  # chemin pour aller à la pièce suivante
directions = [xdep, -xdep, ydep, -ydep, zdep, -zdep]

def pos(x, y, z):
    """Convertir x,y et z en position dans la liste des cubes"""
    return x+y*ydep+z*zdep

def place(cube, position, direction, longueur, Numpiece):
    """Placer un segment dans le cube"""
    Numpiece = int()
    longueur = int()
    for _ in range(longueur):
        position += direction
        assert cube[position] == empty
        cube[position] = Numpiece
        Numpiece += 1
    return position

def unplace(cube, position, direction, longueur):
    """supprimer un segment du cube"""
    for _ in range(longueur):
        position += direction
        cube[position] = empty

def moves(position, direction, cube, Numpiece, longueur):
    """renvoyer le mouvement valide pour la position actuelle"""
    Mvalides = []
    for Ndirections in directions:
        # Impossible de continuer dans la même direction ou l'inverse de la même direction
        if Ndirections == direction or Ndirections == -direction:
            continue
        if valid(numeroCube, position, snake, cube):
            Mvalides.append(Ndirections)
    return Mvalides

def solve(cube, position, direction, snake, Numpiece):
    """le solveur de cube"""
    serpent = len(snake)
    if len(snake) == serpent:
        print("Solution")
        print(visualisationCube(cube))
        return
    longueur, snake = snake[0], snake[1:]
    Mvalides = moves(position, direction, cube, Numpiece, longueur)
    for Ndirections in Mvalides:
        Nposition = place(cube, position, Ndirections, longueur, Numpiece)
        solve(cube, Nposition, Ndirections, snake, Numpiece+longueur)
        unplace(cube, position, Ndirections, longueur)
        

def main(pos, xdep, snake, cube, place, solve):
    # La première pièce doit être placée le long d'un bord
    position = pos(0,1,1)
    direction = xdep
    longueur = snake[0]
    position = place(cube, position, direction, longueur, 1)
    solve(cube, position, direction, snake[1:], longueur + 1)
    

if __name__ == "__main__":
    main(pos, xdep, snake, cube, place, solve)
