from pyplasm import*

def structure(pillarDistance, pillarSection, beamDistance, beamSection):

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


	VIEW(STRUCT([xyzPillar, xyzBeam]))

def inputStructure():
	print("Insert distances between axes of the pillars")
	stringa = raw_input()
	inputList = stringa.split()
	distanzaTraPilastri = [float(x) for x in inputList]

	print("Insert interstory heights")
	stringa = raw_input()
	inputList = stringa.split()
	distanzaTraBasi = [float(x) for x in inputList]

	print("Insert dimensions of beam section")
	stringa = raw_input()
	inputList = stringa.split()
	beamSection = [float(x) for x in inputList]
	beamSection = tuple(beamSection)

	print("Insert dimensions of pillar section)")
	stringa = raw_input()
	inputList = stringa.split()
	pillarSection = [float(x) for x in inputList]
	pillarSection = tuple(pillarSection)

	structure(pillarDistance, pillarSection, beamDistance, beamSection)

#variabili
pillarDistance = [3,4,5]
pillarSection = (0.4,0.4)		#[0] px [1] py
beamDistance = [3,4,2]
beamSection = (2,0.2)			#[0] bx [1] bz
scelta = input('Inserire i valori della struttura manualmente o eseguire esempio? [1/2]:')
if (scelta == 1):
	inputStructure()
else:
	structure(pillarDistance, pillarSection, beamDistance, beamSection)