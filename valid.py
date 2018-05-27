def valid(numeroCube,position,snake,cube):
	if (cube[position]) != 0:
		return False
	else:
		cubePositif = positif(cube)
		if coherence(numeroCube,position,snake,cubePositif):
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
	numeroCube1 = numeroCube - 1 # variable du numéro du cube précédente
	numeroCube2 = numeroCube - 2 # variable du numéro du cube précédente du cube précédente
	positionCube1 = snake.index[numeroCube1]# variable de la position du cube précédent
	positionCube2 = snake.index[numeroCube2]# variable de la position du cube précédent du cube précédente
	save1 = int() #variable pour stocker le i précédent
	verif = bool()
	#variable de déplacement dans le plan :
	x = 1
	y = 5
	z = 5*5

        if numeroCube == 2 : # première solution pour le deuxième cube cube
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

        
        elif numeroCube >= 3: # deuxième solution pour le 3eme cube
            if alignes(position,posistionCube1,positionCube2):
                verif = True
            elif angleDroit(position,positionCube1,positionCube2):
                verif = False
            else:
                return False

            for i in range(len(cubePositif)):
                test += cubePositif[i]
                if i >=1:
                    save1 += cubePositif[i-1]
                
                if verif:
                    if numeroCube <= test and cubePositif[i] > 1 and save1< numeroCube1 <= test:
                        return True
                    else:
                        return False
                else:
                    if numeroCube <= test and cubePositif[i] > 1 and save1< numeroCube1 <= test:
                        return False
                    else:
                        return True
                    
                

        else: #troisième solution c'est le premier cube
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
        
	
