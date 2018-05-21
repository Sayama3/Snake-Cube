def valid(numeroCube,position,snake,cube):
	if snake[position] != 0:
		return -1
	else:
		cubePositif = positif(cube)
		coherence(numeroCube,position,snake,cubePositif)

def positif(cube): #transformer le cube en valeur positif
	import math
	cubePositif = list()
	for i in cube:
		i = int( math.fabs(i) )
		cubePositif.append(i)
		return cubePositif

def coherence(numeroCube,position,snake,cubePositif):
	test = 0 #variable de test afin de vérifier si la position est comprise dedans
	numeroCube1 = numeroCube - 1 # variable de la position précédente
	numeroCube2 = numeroCube - 2 # variable de la position précédente de la position précédente
	positionCube1 = snake.index[numeroCube1]
	positionCube2 = snake.index[numeroCube2]
	
	
	if numeroCube >= 3:
		for i in range( cubePositif ):
			test += cubePositif[i]
			
			
			
			
			if numeroCube == test :
				if alignes(position, positionCube1, positionCube2) == True:
					return True
				else:
					return False
			
			elif numeroCube < test :
			
				
				
				
	elif numeroCube == 2 :
		
	else :
		return True

def alignes(position, cube1, cube2):
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	#vérification que le cube précédent et le cube qui précède le précédent sont alignés, sinon la fonction est fausse
	if cube1 == position - x:
		if cube2 == cube1 - x:
			return True
		else:
			return False
	elif cube1 == position - y:
		if cube2 == cube1 - y:
			return True
		else:
			return False
	elif cube1 == position - z:
		if cube2 == cube1 - z:
			return True
		else:
			return False
	else:
		return False
	
def angledroit(position,cube1,cube2):
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	#vérification que vers le cube précédent et celui qui précède le précédent il y a un angle droit qq part,
	#sinon la fonction est fausse
	if cube1 == position - x:
		if cube2 == cube1 - y:
			return True
		if cube2 == cube1 - z:
			return True
		else:
			return False
	elif cube1 == position - y:
		if cube2 == cube1 - x:
			return True
		if cube2 == cube1 - z:
			return True
		else:
			return False
	elif cube1 == position - z:
		if cube2 == cube1 - x:
			return True
		if cube2 == cube1 - y:
			return True
		else:
			return False
	else:
		return False
	
