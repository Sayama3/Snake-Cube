from math import *
def valid(numeroCube,position,snake,cube):
	if snake[position] != 0:
		return -1
	else:
		cubePositif = positif(cube)
		position(numeroCube,position,snake,cubePositif)

def positif(cube): #transformer le cube en valeur positif
	cubePositif = list()
	for i in cube:
		i = int( fabs(i) )
		cubePositif.append(i)
		return cubePositif

def coherence(numeroCube,position,snake,cubePositif):
	test = 0 #variable de test afin de vérifié si la position est comprise dedans
	position1 = position - 1 # variable de la position précédente
	position2 = position - 2 # variable de la position précédente de la position précédente
	if position >= 3:
		for i in range( sum(cubePositif) ):
			test += cubePositif[i]
			if position == test :
				
			elif position < test :
				
				
				
	else :
		return TRUE
		
		
	
	
