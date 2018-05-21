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
	test = 0 #variable de test afin de vérifié si la position est comprise dedans
	numeroCube1 = numeroCube - 1 # variable de la position précédente
	numeroCube2 = numeroCube - 2 # variable de la position précédente de la position précédente
	cube1 = snake.index[numeroCube1]
	cube2 = snake.index[numeroCube2]
	
	#variable de déplacement dans le plan
	x = 1
	y = 5
	z = 5*5
	
	if numeroCube >= 3:
		for i in range( cubePositif ):
			test += cubePositif[i]
			if numeroCube == test :
				
			elif numeroCube < test :
				
				
				
	elif numeroCube == 2 :
		
	else :
		return TRUE

def alignes():
	if cube1 == position - x:
		
	
