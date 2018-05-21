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

def position(numeroCube,position,snake,cubePositif):
	
	
