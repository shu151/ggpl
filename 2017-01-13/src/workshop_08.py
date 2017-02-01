from pyplasm import *
import csv

def ggpl_house():
	"""
	ggpl_house restituisce un modello hpc di una casa a partire dalla letture dei file .lines
	@return home: modello hpc della struttura
	"""

	# .lines ogni riga ha due coppie di x/y che costituiscono un segmento
	verts = []
	cells = []
	i = 0
	reader = csv.reader(open("lines/muri_esterni.lines", 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	externalWalls = MKPOL([verts,cells,None])
	floor = SOLIDIFY(externalWalls)
	floor = S([1,2,3])([.04,.04,.04])(floor)
	externalWalls = S([1,2,3])([.04,.04,.04])(externalWalls)
	externalWalls = OFFSET([.2,.2,4])(externalWalls)
	heightWalls = SIZE([3])(externalWalls)[0]
	thicknessWalls = SIZE([2])(externalWalls)[0]

	verts = []
	cells = []
	i = 0
	reader = csv.reader(open("lines/muri_interni.lines", 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	internalWalls = MKPOL([verts,cells,None])
	internalWalls = S([1,2,3])([.04,.04,.04])(internalWalls)
	internalWalls = OFFSET([.2,.2,4])(internalWalls)
	walls = STRUCT([externalWalls, internalWalls])

	verts = []
	cells = []
	i = 0
	reader = csv.reader(open("lines/porte.lines", 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	doors = MKPOL([verts,cells,None])
	doors = SOLIDIFY(doors)
	doors = S([1,2,3])([.04,.04,.04])(doors)
	doors = OFFSET([.2,.2,3])(doors)
	walls = DIFFERENCE([walls, doors])


	verts = []
	cells = []
	i = 0
	reader = csv.reader(open("lines/finestre.lines", 'rb'), delimiter=',')  
	for row in reader:
		verts.append([float(row[0]), float(row[1])])
		verts.append([float(row[2]), float(row[3])])
		i+=2
		cells.append([i-1,i])

	windows = MKPOL([verts,cells,None])
	windows = SOLIDIFY(windows)
	windows = S([1,2,3])([.04,.04,.04])(windows)
	windows = OFFSET([.2,.2,2])(windows)
	heightWindows = SIZE([3])(windows)[0]
	windows = T(3)((heightWalls-heightWindows)/2.)(windows)
	walls = DIFFERENCE([walls, windows])

	floor = TEXTURE("texture/floor.jpg")(floor)
	walls = TEXTURE("texture/wall.jpg")(walls)
	home = STRUCT([floor, walls])
	return home


VIEW(ggpl_house())