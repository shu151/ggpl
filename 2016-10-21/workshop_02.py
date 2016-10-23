from pyplasm import*
import csv


def ggpl_bone_structure(file_name):
	"""
	gpl_bone_structure crea una struttura secondo i parametri descritti nel file_name

	@param file_name: stringa della directory del file
	@return result: la struttura finale
	"""

	def readCsv(file_name):
		"""
		readCsv legge i dati all'interno del file_name e ritorna un yield con i campi recuperati dal file

		@param file_name: stringa della directory del file
		@return result: yield con i valori estratti
		"""
		riga = 0
		reader = csv.reader(open(file_name, 'r'), delimiter=';')  
		for row in reader:
			if(riga==1):
				pillarDistance = (row[0].split(','))
				i = 0
				for el in pillarDistance:
					pillarDistance[i] = float(el)
					i = i+1
				pillarSection = (row[1].split(','))
				i = 0
				for el in pillarSection:
					pillarSection[i] = float(el)
					i = i+1
				pillarSection = tuple(pillarSection)
				beamDistance = (row[2].split(','))
				i = 0
				for el in beamDistance:
					beamDistance[i] = float(el)
					i = i+1
				beamSection = (row[3].split(','))
				i = 0
				for el in beamSection:
					beamSection[i] = float(el)
					i = i+1
				beamSection = tuple(beamSection)
				riga = riga-1
				yield pillarDistance, pillarSection, beamDistance, beamSection, vector
			else:
				vector = [float(row[0]), float(row[1]), float(row[2])]
				riga = riga+1

	def structure(pillarDistance, pillarSection, beamDistance, beamSection):
		"""
		structure restituisce un frame secondo le specifiche del workshop 01

		@param pillarDistance: lista delle distance da un pilastro all'altro
		@param pillarSection: una tupla della dimensione del pilastro (px,py)
		@param beamDistance: lista delle distanze da una trave all'altra
		@param beamSection: tupla della dimensione di una trave (bx,bz)
		@return result: la struttura del frame
		"""
		pillarList = []
		for dist in pillarDistance:
			pillarList.append(pillarSection[1])
			pillarList.append(dist-dist*2)
		pillarList.append(pillarSection[1])

		pillarDistanceSum = sum([abs(i) for i in pillarDistance])

		beamList = []
		for dist in beamDistance:
			beamList.append(dist-dist*2)
			beamList.append(beamSection[1])

		centrarePilastroNellaBase = (beamSection[0]-pillarSection[0])/2
		xPillar = QUOTE(pillarList)
		if centrarePilastroNellaBase >= 0:
			yPillar = QUOTE([-centrarePilastroNellaBase,pillarSection[0],-centrarePilastroNellaBase])
		else:
			yPillar = QUOTE([pillarSection[0]])
		xyPillar = PROD([xPillar,yPillar])
		xyzPillar = PROD([xyPillar, QUOTE(-i for i in beamList)]) #serve per creare pilastri di altezza corretta con la lista beam invertita di segno

		xBeam = QUOTE([pillarDistanceSum+pillarSection[1]*(len(pillarDistance)+1)])
		if centrarePilastroNellaBase >= 0:
			yBeam = QUOTE([beamSection[0]])
		else:
			yBeam = QUOTE([centrarePilastroNellaBase,beamSection[0],centrarePilastroNellaBase])
		xyBeam = PROD([xBeam, yBeam])
		xyzBeam = PROD([xyBeam, QUOTE(beamList)])

		return [xyzPillar, xyzBeam]

	def beamLinkStructure(pillarDistance, pillarSection, beamDistance, beamSection, vector):
		"""
		beamLinkStructure restituisce le travi di collegamento da un frame al frame successivo

		@param pillarDistance: lista delle distance da un pilastro all'altro
		@param pillarSection: una tupla della dimensione del pilastro (px,py)
		@param beamDistance: lista delle distanze da una trave all'altra
		@param beamSection: tupla della dimensione di una trave (bx,bz)
		@param vector: e' un vettore che indica lo spostamento da un frame al successivo
		@return result: la struttura del frame
		"""

		pillarList = []
		for dist in pillarDistance:
			pillarList.append(pillarSection[1])
			pillarList.append(dist-dist*2)
		pillarList.append(pillarSection[1])

		beamList = []
		for dist in beamDistance:
			beamList.append(dist-dist*2)
			beamList.append(beamSection[1])

		xBeamLink = QUOTE(pillarList)
		yBeamLink = QUOTE([-beamSection[0], vector[0]])
		xyBeamLink = PROD([xBeamLink, yBeamLink])
		xyzBeamLink = PROD([xyBeamLink, QUOTE(beamList)])

		return xyzBeamLink


	lista = []
	primpoFrame = TRUE
	for pillarDistance, pillarSection, beamDistance, beamSection, vector in readCsv(file_name):

		stru = structure(pillarDistance, pillarSection, beamDistance, beamSection)
		link = beamLinkStructure(pillarDistance, pillarSection, beamDistance, beamSection, vector)
		
		if(primpoFrame==TRUE):
			lista.append(T(2)((vector[0])))
			primpoFrame = FALSE
		else:
			lista.append(link)
			lista.append(T(2)((vector[0])+beamSection[0]))

		lista.append(stru[0])
		lista.append(stru[1])
	result = (STRUCT(lista))
	return result

VIEW(ggpl_bone_structure("frame_data_464999.csv"))