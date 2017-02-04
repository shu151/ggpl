from pyplasm import *
from src import workshop_07 as doorAndWindow
from src import workshop_03 as stair
from src import workshop_09 as roofMain
import math
import csv
import os

X = [.1,.2,0.05,.2,.1,.1,.2,0.05,.2,.1]
Y = [.1,.3,.05,.35,.05,0.3,0.1]
Z = [0.0,3.0,8.0,10.0]
occupancy = [[True, True, True, True, True, True, True],
		  [True, False, True, False, True, False, True],
		  [True, True, True, True, True, True, True],
		  [True, False, True, False, True, False, True],
		  [True, True, True, True, True, True, True],
		  [True, True, True, True, True, True, True],
		  [True, False, True, False, True, False, True],
		  [True, True, True, True, True, True, True],
		  [True, False, True, False, True, False, True],
		  [True, True, True, True, True, True, True]]


def multistorey_house(storey):
	"""
	multistorey_house prende in input il numero di piani della casa e restituisce l'HPC della casa generata
	@param storey: numero dei piani
	@return house: l'HPC della casa
	"""
	def buildExternalWalls(heightWalls, textureWallsFile):
		"""
		buildExternalWalls prende in input l'altezza di un piano della casa
		@param heightWalls: altezza piano
		"""
		def buildDoors(heightDoors):
			"""
			buildDoors prende in input l'altezza delle porte
			@param heightDoors: altezza porte
			"""
			def buildWindows(heightWindows):
				"""
				buildWindows prende in input l'altezza delle finestre
				@param heightWindows: altezza finestre
				"""
				def buildRoof(pendenzaFalda, textureRoofFile):
					"""
					buildRoof prende in input la pendenza delle falde del tetto
					@param pendenzaFalda: la pendenza in gradi delle falde del tetto
					"""
					floors = []
					walls = []
					holeDoors = []
					doors = []
					holeWindows = []
					windows = []
					stairs=[]


					for i in range(storey):
						floor = createFloor("lines/muri_esterni.lines")
						floors.append(T([3])([heightWalls*(i)])(floor))

						externalWall = createWall("lines/muri_esterni.lines",heightWalls,textureWallsFile)
						internalWall = createWall("lines/muri_interni.lines",heightWalls,textureWallsFile)
						walls.append(T([3])([heightWalls*(i)])(externalWall))
						walls.append(T([3])([heightWalls*(i)])(internalWall))

						holeDoorsPlane = createHoleDoors("lines/porte"+str(i+1)+".lines",heightDoors,walls)
						if (holeDoorsPlane!=None):
							holeDoors.append(T([3])([heightWalls*(i)])(holeDoorsPlane))

						doorsPlane = createDoors("lines/porte"+str(i+1)+".lines",heightDoors,walls)
						if (doorsPlane!=None):
							doors.append(T([3])([heightWalls*(i)])(doorsPlane))

						holeWindowsPlane = createHoleWindows("lines/finestre_dett.lines",heightWindows,heightWalls,walls)
						holeWindows.append(T([3])([heightWalls*(i)])(holeWindowsPlane))

						windowsPlane = createWindows("lines/finestre_dett.lines",heightWindows,heightWalls,walls)
						windows.append(T([3])([heightWalls*(i)])(windowsPlane))

						stair = createStairs("lines/scala"+str(i+1)+".lines",heightWalls)
						if (stair!=None):
							stairs.append(stair)


					roof = createRoof("lines/muri_esterni.lines",heightWalls*storey,pendenzaFalda,textureRoofFile)

					floors = STRUCT(floors)
					walls = STRUCT(walls)
					holeDoors = STRUCT(holeDoors)
					walls = DIFFERENCE([walls, holeDoors])
					doors = STRUCT(doors)
					holeWindows = STRUCT(holeWindows)
					walls = DIFFERENCE([walls, holeWindows])
					walls = TEXTURE("texture/wall.jpg")(walls)
					windows = STRUCT(windows)

					if not stairs:
						house = STRUCT([floors,walls,doors,windows,roof])
					else:
						stairs = STRUCT(stairs)
						house = STRUCT([floors,walls,doors,windows,stairs,roof])
					return house
				return buildRoof
			return buildWindows
		return buildDoors
	return buildExternalWalls

def createStairs(file,heightWalls):
	"""
	createStairs prende in input il nome del file e l'altezza dei muri
	@param file: nome del file da cui prendere i vari parametri
	@param heightWalls: altezza dei muri
	@return stairList: l'HPC delle scale
	"""
	if os.path.isfile(file):
		reader = csv.reader(open(file, 'rb'), delimiter=',')  
		i = 0
		scale=[]
		for row in reader:
			if((i)%4==0):
				minX=min([float(row[0]),float(row[2])])
				maxX=max([float(row[0]),float(row[2])])
				minY=min([float(row[1]),float(row[3])])
				maxY=max([float(row[1]),float(row[3])])
				i=i+1
			elif((i)%4!=0 and (i+1)%4==0):
				minX=min(min([float(row[0]),float(row[2])]),minX)
				maxX=max(max([float(row[0]),float(row[2])]),maxX)
				minY=min(min([float(row[1]),float(row[3])]),minY)
				maxY=max(max([float(row[1]),float(row[3])]),maxY)
				scala = []
				scala.append(minX)
				scala.append(maxX)
				scala.append(minY)
				scala.append(maxY)
				scale.append(scala)
				i=i+1
			elif((i)%4!=0):
				minX=min(min([float(row[0]),float(row[2])]),minX)
				maxX=max(max([float(row[0]),float(row[2])]),maxX)
				minY=min(min([float(row[1]),float(row[3])]),minY)
				maxY=max(max([float(row[1]),float(row[3])]),maxY)
				i=i+1

		stairList = []
		for scalaP in scale:
			dx=scalaP[1]*0.04-scalaP[0]*0.04
			dy=scalaP[3]*0.04-scalaP[2]*0.04
			dz=heightWalls
			kkk= stair.ggpl_straight_stairs(dx, dy, dz)
			stairList.append(T(1)(scalaP[0]*0.04))
			stairList.append(T(2)(scalaP[2]*0.04))
			stairList.append(kkk)
			stairList.append(T(1)(-scalaP[0]*0.04))
			stairList.append(T(2)(-scalaP[2]*0.04))

		stairList = STRUCT(stairList)
		stairList = TEXTURE("texture/stair.jpg")(stairList)
		return stairList
	return None


def createHoleWindows(file,heightWindows,heightWalls,walls):
	"""
	createHoleWindows prende in input il nome del file, l'altezza della finestra e i muri
	@param file: nome del file da cui prendere i vari parametri
	@param heightWindows: altezza delle finestre
	@param walls: HPC dei muri
	@return holeWindows: l'HPC delle posizioni delle finestre
	"""
	holeWindows = []
	reader = csv.reader(open(file, 'rb'), delimiter=',')  
	for row in reader:
		holeWindow = POLYLINE([[float(row[0]), float(row[1])], [float(row[2]), float(row[3])]])
		if (row[1] == row[3]):
			holeWindow = S([1,2,3])([.04,.04,.04])(holeWindow)
			holeWindow = OFFSET([0,1,heightWindows])(holeWindow)
			holeWindow = T([2])([-0.5])(holeWindow)
			holeWindows.append(holeWindow)


	holeWindows = STRUCT(holeWindows)
	holeWindows = T(3)((heightWalls-heightWindows)/2.)(holeWindows)
	return holeWindows

def createWindows(file,heightWindows,heightWalls,walls):
	"""
	createWindows prende in input il nome del file, l'altezza della finestre, dei muri e i muri
	@param file: nome del file da cui prendere i vari parametri
	@param heightWindows: altezza delle finestre
	@param heightWalls: altezza dei muri
	@param walls: HPC dei muri
	@return finestre: l'HPC delle porte
	"""
	reader = csv.reader(open("lines/finestre_dett.lines", 'rb'), delimiter=',')  
	finestre = []
	for row in reader:
		if(row[0]==row[2]):
			dx=0.2
			dy=max([float(row[1]),float(row[3])])-min([float(row[1]),float(row[3])])
			dz=(heightWalls-heightWindows)/2.
			finestra=doorAndWindow.createWindowXAxis(X,Y,Z,occupancy,dx,dy,dz)
			finestre.append(T(1)(float(row[0])*0.04))
			finestre.append(T(2)(float(row[1])*0.04))
			finestre.append(T(3)(((heightWalls-heightWindows)/2.)))
			finestre.append(S([1,2,3])([.04,.04,.04])(finestra))
			finestre.append(T(1)(-float(row[0])*0.04))
			finestre.append(T(2)(-float(row[1])*0.04))
			finestre.append(T(3)(-((heightWalls-heightWindows)/2.)))
		if(row[1]==row[3]):
			dx=max([float(row[0]),float(row[2])])-min([float(row[0]),float(row[2])])
			dy=dx/13.33
			dz=heightWindows/0.04
			finestra=doorAndWindow.createWindowXAxis(X,Y,Z,occupancy,dx,dy,dz)
			finestre.append(T(1)(float(row[0])*0.04))
			finestre.append(T(2)(float(row[1])*0.04))
			finestre.append(T(3)(((heightWalls-heightWindows)/2.)))
			finestre.append(S([1,2,3])([.04,.04,.04])(finestra))
			finestre.append(T(1)(-float(row[0])*0.04))
			finestre.append(T(2)(-float(row[1])*0.04))
			finestre.append(T(3)(-((heightWalls-heightWindows)/2.)))

	finestre=STRUCT(finestre)

	return finestre

def createHoleDoors(file,heightDoors,walls):
	"""
	createHoleDoors prende in input il nome del file, l'altezza della porta e i muri
	@param file: nome del file da cui prendere i vari parametri
	@param heightDoors: altezza delle porte
	@param walls: HPC dei muri
	@return holeDoors: l'HPC delle posizioni delle porte
	"""
	if os.path.isfile(file):
		holeDoors = []
		reader = csv.reader(open(file, 'rb'), delimiter=',')  
		for row in reader:
			holeDoor = POLYLINE([[float(row[0]), float(row[1])], [float(row[2]), float(row[3])]])
			if (row[1] == row[3]):
				holeDoor = S([1,2,3])([.04,.04,.04])(holeDoor)
				holeDoor = OFFSET([0,1,heightDoors])(holeDoor)
				holeDoor = T([2])([-0.5])(holeDoor)
				holeDoors.append(holeDoor)
			elif (row[0] == row[2]):
				holeDoor = S([1,2,3])([.04,.04,.04])(holeDoor)
				holeDoor = OFFSET([1,0,heightDoors])(holeDoor)
				holeDoor = T([1])([-0.5])(holeDoor)
				holeDoors.append(holeDoor)

		holeDoors = STRUCT(holeDoors)
		return holeDoors
	return None

def createDoors(file,heightDoors,walls):
	"""
	createDoors prende in input il nome del file e l'altezza della porta e i muri
	@param file: nome del file da cui prendere i vari parametri
	@param heightDoors: altezza delle porte
	@param walls: HPC dei muri
	@return doors: l'HPC delle porte
	"""
	if os.path.isfile(file):
		reader = csv.reader(open(file, 'rb'), delimiter=',')
		doors = []
		for row in reader:
			if(row[0]==row[2]):
				dy=max([float(row[1]),float(row[3])])-min([float(row[1]),float(row[3])])
				dx=dy/13.33
				dz=heightDoors/0.04
				door=doorAndWindow.createDoorYAxis(X,Y,Z,occupancy,dy,dx,dz)
				doors.append(T(1)(float(row[0])*0.04))
				doors.append(T(2)(float(row[1])*0.04))
				doors.append(S([1,2,3])([.04,.04,.04])(door))
				doors.append(T(1)(-float(row[0])*0.04))
				doors.append(T(2)(-float(row[1])*0.04))
			elif(row[1]==row[3]):
				dx=max([float(row[0]),float(row[2])])-min([float(row[0]),float(row[2])])
				dy=dx/13.33
				dz=heightDoors/0.04
				door=doorAndWindow.createDoorXAxis(X,Y,Z,occupancy,dx,dy,dz)
				doors.append(T(1)(float(row[0])*0.04))
				doors.append(T(2)(float(row[1])*0.04))
				doors.append(S([1,2,3])([.04,.04,.04])(door))
				doors.append(T(1)(-float(row[0])*0.04))
				doors.append(T(2)(-float(row[1])*0.04))

		doors = STRUCT(doors)
		return doors
	return None


def createWall(file,heightWalls,textureWallsFile):
	"""
	createWall prende in input il nome del file e l'altezza del muro
	@param file: nome del file da cui prendere i vari parametri
	@param heightWalls: altezza del muro
	@return walls: l'HPC dei muri
	"""
	verts = []
	cells = []
	i = 0
	reader = csv.reader(open(file, 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	walls = MKPOL([verts,cells,None])
	walls = S([1,2,3])([.04,.04,.04])(walls)
	walls = OFFSET([.2,.2,heightWalls])(walls)
	walls = TEXTURE(textureWallsFile)(walls)
	return walls


def createFloor(file):
	"""
	createFloor prende in input il nome del file
	@param file: nome del file da cui prendere i vari parametri
	@return floor: l'HPC del pavimento
	"""
	# .lines ogni riga ha due coppie di x/y che costituiscono un segmento
	verts = []
	cells = []
	i = 0
	reader = csv.reader(open(file, 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	externalWalls = MKPOL([verts,cells,None])
	floor = SOLIDIFY(externalWalls)
	floor = S([1,2,3])([.04,.04,.04])(floor)
	floor = TEXTURE("texture/floor.jpg")(floor)
	return floor

def createRoof(file,heightHouse,pendenzaFalda,textureRoofFile):
	"""
	createRoof prende in input il nome del file, l'altezza della casa e la pendenza della falda del tetto
	@param file: nome del file da cui prendere i vari parametri
	@param heightHouse: altezza della casa
	@param pendenzaFalda: pendenza della falda del tetto
	@return roof: l'HPC del tetto
	"""
	verts = []
	cells = []
	i = 0
	reader = csv.reader(open(file, 'rb'), delimiter=',')  
	for row in reader:
		if(i==0):
			verts.append([float(row[0])*0.04, float(row[1])*0.04,0])
		verts.append([float(row[2])*0.04, float(row[3])*0.04,0])
		i+=2
		cells.append([i-1,i])

	roof = roofMain.ggpl_roof(verts,pendenzaFalda,4,[1,2,3,1,3,1])
	roof = OFFSET([.2,.2,0])(roof)
	roof = (T(3)(heightHouse)(roof))
	roof = TEXTURE(textureRoofFile)(roof)
	return roof


#VIEW(multistorey_house(3)(5,"texture/wall.jpg")(3)(2)(PI/6,"texture/roofing.jpg"))
VIEW(multistorey_house(2)(4,"texture/wall.jpg")(3)(2)(PI/4,"texture/roofing.jpg"))