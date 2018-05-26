def valid(numeroCube,position,snake,cube):
	if (cube[position]) != 0:
		return False
	else:
		cubePositif = positif(cube)
		if coherence(numeroCube,position,snake,cubePositif) == True:
			return True
		else:
			return False

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
	save1 = int() #variable pour stocker i
	save2 = int() #variable pour stocker i
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	#vérification alignement ou angle droit
	if numeroCube >= 3:
		for i in range( cubePositif ):
			test += cubePositif[i]
			
			
			
			#vérification alignement
			if numeroCube == test :
				if alignes(position, positionCube1, positionCube2):
					return True
				else:
					return False
			#vérification alignement ou angle droit
			elif numeroCube < test :
				
				if numeroCube1 <= test - cubePositif[i]:
					save1 = test - cubePositif[i]
				else:
					save1 = test
				if numeroCube2 <= test - cubePositif[i]:
					save2 = test - cubePositif[i]
				else:
					save2 = test
				 
				if test == save1 :
					if test == save2:
						if alignes(position, positionCube1, positionCube2):
							return True
						else:
							return False
					elif test == save2 + cubePositif[i]:
						if angleDroit(position, positionCube1, positionCube2):
							return True
						else:
							return False 
					else:
						return false
				elif test == save1 + cubePositif[i]:
					if save1 == save2:
						if angleDroit(position, positionCube1, positionCube2):
							return True
						else:
							return False 
					else:
						return False
				else:
					return False
				
				
				
	#vérification pour le 2ème cube s'il se positionne bien			
	elif numeroCube == 2 :
		if positionCube1 - x == position:
			return True
		elif positionCube1 + x == position:
			return True
		elif positionCube1 - y == position:
			return True
		elif positionCube1 + y == position:
			return True
		elif positionCube1 - z == position:
			return True
		elif positionCube1 + z == position:
			return True
		else:
			return False
		
		
	else :
		return True

def alignes(position, cube1, cube2):
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	#vérification que le cube précédent et le cube qui précède le précédent sont alignés, sinon la fonction est fausse
	if cube1 == position - x or cube1 == position + x:
		if cube2 == cube1 - x or cube1 == position + x:
			return True
		else:
			return False
	elif cube1 == position - y or cube1 == position + y:
		if cube2 == cube1 - y or cube1 == position + y:
			return True
		else:
			return False
	elif cube1 == position - z or cube1 == position + z:
		if cube2 == cube1 - z or cube1 == position + z:
			return True
		else:
			return False
	else:
		return False
	
def angleDroit(position,cube1,cube2):
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	#vérification que vers le cube précédent et celui qui précède le précédent il y a un angle droit qq part,
	#sinon la fonction est fausse
	if cube1 == position - x or cube1 == position + x:
		if cube2 == cube1 - y or cube1 == position + y:
			return True
		if cube2 == cube1 - z or cube1 == position + z:
			return True
		else:
			return False
	elif cube1 == position - y or cube1 == position + y:
		if cube2 == cube1 - x or cube1 == position + x:
			return True
		if cube2 == cube1 - z or cube1 == position + z:
			return True
		else:
			return False
	elif cube1 == position - z or cube1 == position + z:
		if cube2 == cube1 - x or cube1 == position + x:
			return True
		if cube2 == cube1 - y or cube1 == position + y:
			return True
		else:
			return False
	else:
		return False

if __name__ == '__main__':
        cube = [5, 4, -3, 3, 4, 1, 1, -4, 2]
        cube2 = positif(cube)
        
	
