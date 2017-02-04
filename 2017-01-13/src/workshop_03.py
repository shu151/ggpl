from pyplasm import *
import math

def ggpl_l_shaped_stair(dx, dy, dz):
	"""
	ggpl_l_shaped_stair crea una scala "L shaped" secondo i parametri dx dy dz che indicano le dimensioni della scatola in cui
	la scala deve rientrare

	@param dx,dy,dz: valori(float) della dimensione della scatola
	@return stair: la scala "L shaped"
	"""

	def stairRamp(dx,dy,dz,stairRampObjectList,yNumeroGradini,zNumeroGradini,dxGradino,dyGradino,dzGradino):
		"""
		stairRamp crea una lista che contiene i valori per creare una rampa di scale

		@param dx,dy,dz: valori(float) della dimensione della scatola
		@param stairRampObjectList: e' la lista in cui si inseriranno i valori della rampa di scale
		@param yNumeroGradini: e' il numero di gradini che bisogna inserire nella rampa di scale
		@param zNumeroGradini: e' il numero di gradini che ancora si possono inserire prima di arrivare a dz
		@param dxGradino: indica la larghezza della rampa
		@param dyGradino: indica la pedata (tread) della scala
		@param dzGradino: indica di quanto bisogna alzare il successivo gradino(la meta' e' quindi all'incirca l'alzata (riser))
		@return stairRampObjectList: lista contentente i valori per creare una rampa di scale
		"""
		xyGradino = MKPOL([[[0,0],[0,dzGradino],[dyGradino,dzGradino],[dyGradino,dzGradino/2],[0,0]],[[1,2,3,4,5]],1])
		xyzGradino = PROD([QUOTE([dxGradino]),xyGradino])

		for i in range(yNumeroGradini):
			stairRampObjectList.append(xyzGradino)
			zNumeroGradini = zNumeroGradini-1
			# se non ho spazio lungo l'asse z smetto di inserire gradini ritorno la rampa
			if zNumeroGradini<=0:
				return stairRampObjectList
			stairRampObjectList.append(T([2,3])([dyGradino,dzGradino-0.2]))	#attenzione il -0.2 e' in relazione al dxGradino in ggpl_l_shaped_stair che vale 0.4
		stairRampObjectList.append(CUBOID([dxGradino,dxGradino-dyGradino,dzGradino-0.2]))
		stairRampObjectList.append(T([2])([dxGradino-dyGradino]))
		stairRampObjectList.append(R([2,1])(PI/2))
		stairRampObjectList.append(T([2])([dxGradino]))
		return stairRampObjectList

	stairRampObjectList = []
	stair = []
	# dimensioni di partenza per la creazione di un gradino che sono poi modificate per poter riempire in modo esatto la scatola
	dxGradino = 1
	dyGradino = 0.3
	dzGradino = 0.4

	#box = SKEL_1(CUBOID([dx,dy,dz]))
	#stair.append(box)
	# crea il primo platform
	stairRampObjectList.append(CUBOID([dxGradino,dxGradino,dzGradino-0.2]))
	stairRampObjectList.append(T([2])([dxGradino]))

	# indica su quale coordinata si trova la rampa (latoX=0  ==> dy) (latoX=1  ==> dx)
	latoX=0
	zNumeroGradiniNonIntero = (dz-(dzGradino/2))/(dzGradino/2)
	zNumeroGradini = (int)(math.floor(zNumeroGradiniNonIntero))
	# indica quanto spazio rimane per riempire la scatola inserendo le dimensioni di base di un gradino
	dzScarto = (dz-(zNumeroGradini*dzGradino+dzGradino/2))/zNumeroGradini
	# e' l'altezza corretta per riempire la scatola
	dzGradino = dzGradino + dzScarto + dzGradino/2

	# finche ho ancora spazio lungo dz inserisco nuove rampe
	while zNumeroGradini>0:
		if latoX == 0:
			yNumeroGradiniNonIntero = (dy-dxGradino-dxGradino+dyGradino)/dyGradino
			yNumeroGradini = (int)(math.floor(yNumeroGradiniNonIntero))
			dyGradinoConScarto = (dy-dxGradino*2)/(yNumeroGradini-1)
			dyGradino = dyGradinoConScarto
			latoX=latoX+1
		else:
			yNumeroGradiniNonIntero = (dx-dxGradino-dxGradino+dyGradino)/dyGradino
			yNumeroGradini = (int)(math.floor(yNumeroGradiniNonIntero))
			dyGradinoConScarto = (dx-dxGradino*2)/(yNumeroGradini-1)
			dyGradino = dyGradinoConScarto
			latoX=latoX-1
		stairRampObjectList = stairRamp(dx,dy,dz,stairRampObjectList,yNumeroGradini,zNumeroGradini,dxGradino,dyGradino,dzGradino)
		zNumeroGradini = zNumeroGradini - yNumeroGradini
		for el in stairRampObjectList:
			stair.append(el)
		stairRampObjectList = []
	return stair


def ggpl_straight_stairs(dx, dy, dz):
	"""
	ggpl_straight_stairs crea una scala "straight" secondo i parametri dx dy dz che indicano le dimensioni della scatola in cui
	la scala deve rientrare

	@param dx,dy,dz: valori(float) della dimensione della scatola
	@return stair: l'hpc della scala
	"""
	dxGradino = dx
	dyGradino = 0.3
	dzGradino = 0.4

	gradini = dz/dzGradino
	dzGradino = dz/round(gradini,0)
	gradini = (int)(round(gradini,0))*2

	xyGradino = MKPOL([[[0,0],[0,dzGradino],[dyGradino,dzGradino],[dyGradino,dzGradino/2],[0,0]],[[1,2,3,4,5]],1])
	xyzGradino = PROD([QUOTE([dxGradino]),xyGradino])


	stairRampObjectList = []
	stairRampObjectList.append(CUBOID([dxGradino,dyGradino,dzGradino/2]))
	stairRampObjectList.append(T([2])([dyGradino]))
	for i in range(gradini-1):
		stairRampObjectList.append(xyzGradino)
		stairRampObjectList.append(T([2])([dyGradino]))
		stairRampObjectList.append(T([3])([dzGradino/2]))
	return STRUCT(stairRampObjectList)



#VIEW(STRUCT(ggpl_l_shaped_stair(6.0,6.0,24.0)))
#VIEW(ggpl_straight_stairs(6.0,6.0,1.0))



