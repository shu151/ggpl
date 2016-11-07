from pyplasm import *
import math

def ggpl_hip_roof_builder(structure):

	"""
	ggpl_hip_roof_builder crea un tetto a partire dalla struttura dello scheletro che lo sorregge

	@param structure: un hpc che indica la struttura su cui va inserito il tetto
	@return structureFinal: il tetto con la struttura iniziale
	"""

	# ricava i valori di vertici e celle da sistemare tramite UKPOL

	valstruct = UKPOL(structure)
	verts = valstruct[0]
	cells = valstruct[1]

	# arrotonda i punti dei vertici

	for i in range(len(verts)): #i parte da 0
		verts[i][0] = round(verts[i][0],1) #arrotonda per difetto sotto a .50 per eccesso da .50
		verts[i][1] = round(verts[i][1],1)
		verts[i][2] = round(verts[i][2],1)

	# vertsDict come chiave ha il vertice convertito in stringa e come valore ha una lista di due elementi il primo e' un valore progressivo
	# mentre il secondo e' una lista di punti presenti piu volte nella lista verts
	# in questo modo creo una nuova lista di vertici eliminando i duplicati

	vertsDict = {}
	j=1

	# vertsNew sono i nuovi vertici con valori arrotondati e in cui non sono presenti duplicati

	vertsNew = []
	for i in range(len(verts)):
		vertstringKey = str(verts[i][0])+str(verts[i][1])+str(verts[i][2])
		if (vertsDict.has_key(vertstringKey)):
			vertsDict[vertstringKey][1].append(i+1)
		else:
			vertsDict[vertstringKey] = [j,[i+1]]
			vertsNew.append(verts[i])
			j = j+1

	# corregge le celle prese da UKPOL adattandole alla nuova lista dei vertici
	# cellsNew sono le nuove celle corrette in base ai nuovi valori dei vertici
	# cellNew e' una lista di supporto utilizzata per creare cellsNew

	cellsNew = []
	cellNew = []
	for i in range(len(cells)):
		for e in range(len(cells[i])):
			for j in range(len(vertsDict.values())):
				if cells[i][e] in vertsDict.values()[j][1]:
					cellNew.append(vertsDict.values()[j][0])
		cellsNew.append(cellNew)
		cellNew = []

	# prende i vertici che non si trovano nel piano z=0 e li inserisce nella lista vertsTop

	vertsTop = []
	for i in range(len(vertsNew)):
		if vertsNew[i][2] > 0:
			vertsTop.append(vertsNew[i])

	# crea la lista vertsRoof sostituendo i valori interni alla struttura con i valori nel piano z>0 per permettere la creazione delle facciate del tetto
	# vertsRoof e' una lista con solo i valori necessari per la creazione delle facciate

	vertsRoof = []
	for i in range(len(vertsNew)):
		insert = 1
		for j in range(len(vertsTop)):
			if (vertsNew[i][0] == vertsTop[j][0] and vertsNew[i][1] == vertsTop[j][1] and vertsNew[i][2] == 0):
				insert = 0
				vertsRoof.append(vertsTop[j])
		if insert != 0:
			vertsRoof.append(vertsNew[i])
			
	roof = OFFSET([0.1, 0.1, 0.1])((MKPOL([vertsRoof,cellsNew,None])))
	roof = STRUCT([T(3)(0.1),roof])
	structureFinal = []
	skel = OFFSET([0.1, 0.1, 0.1])(SKEL_1(structure))
	structureFinal.append(COLOR(RED)(roof))
	structureFinal.append(skel)
	return STRUCT(structureFinal)

structure = MKPOL([[[0,0,0],[5,0,0],[5,5,0],[15,5,0],[15,10,0],[0,10,0],[2.5,2,4],[2.5,2,0],[2.5,7.5,4],[2.5,7.5,0],[13,7.5,4],[13,7.5,0]],[[1,2,7,8],[1,8,7,9,10,6],[3,10,9,11,12,4],[6,10,9,11,12,5],[5,4,12,11],[2,8,7,9,10,3]],None])
#structure = MKPOL([[[0,0,0],[0,10,0],[2.5,5,0],[2.5,5,5],[15,0,0],[15,10,0],[12.5,5,0],[12.5,5,5]],[[1,2,4,3],[8,5,6,7],[1,3,4,8,7,5],[2,3,4,8,7,6]],None])
VIEW(ggpl_hip_roof_builder(structure))



