from pyplasm import *
from src import workshop_07 as doorAndWindow
from src import workshop_03 as stair
from src import workshop_09 as roofMain
from src import workshop_10 as houseMain
import math
import csv

#VIEW(MAP(BEZIERCURVE([[1,4],[1.1,1.9],[2,1.1],[6,1]]))(INTERVALS(1)(32)))
def street4(streets):
	"""
	street4 inserisce un insieme di strade

	@param streets: lista delle strade di partenza
	@return streets: lista finale delle strade
	"""

	street = MAP(BEZIERCURVE([[452,4],[452,175],[540,160]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[462,4],[462,165],[540,150]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[452,4],[462,4]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[540,160],[540,150]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	return streets


def street3(streets):
	"""
	street3 inserisce un insieme di strade

	@param streets: lista delle strade di partenza
	@return streets: lista finale delle strade
	"""

	#provvisorio
	#street = MAP(BEZIERCURVE([[226,103],[226,100]]))(INTERVALS(1)(32))
	#streets.append(street)

	street = MAP(BEZIERCURVE([[226,100],[240,105],[260,94]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[226,103],[240,108],[260,97]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[255,85],[257,90],[260,94]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[258,85],[260,90],[263,92]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[255,85],[258,85]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[260,97],[263,95]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[263,95],[280,95],[300,83]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[263,92],[280,92],[300,80]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[300,83],[303,95],[300,120]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[303,83],[306,95],[303,120]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va una casa

	street = MAP(BEZIERCURVE([[300,120],[303,120]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[300,80],[310,78],[320,75]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[303,83],[313,80],[320,78]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[323,75],[332,77],[338,75]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[320,78],[329,80],[338,78]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[341,78],[342,87],[341,96]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[338,78],[339,87],[338,96]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#va la casa

	street = MAP(BEZIERCURVE([[338,96],[341,96]]))(INTERVALS(1)(32))
	streets.append(street)

	#
	street = MAP(BEZIERCURVE([[338,75],[341,69],[340,63]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[341,75],[344,69],[343,63]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#street = MAP(BEZIERCURVE([[333,60],[336,60],[340,60]]))(INTERVALS(1)(32))
	#street2 = MAP(BEZIERCURVE([[330,63],[336,63],[340,63]]

	street = MAP(BEZIERCURVE([[341,78],[362,80],[377,78]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[341,75],[362,77],[377,75]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[380,78],[380,83],[380,87]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[377,78],[377,83],[377,87]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[377,87],[380,87]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[380,78],[395,77],[410,78]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[377,75],[395,74],[410,75]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[410,78],[410,83],[410,86]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[413,78],[413,83],[413,86]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[410,86],[413,86]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[413,78],[434,79],[447,78]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[410,75],[434,76],[447,75]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[447,78],[447,75]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[323,75],[321,72],[323,62]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[320,75],[318,72],[320,62]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[320,62],[300,57],[290,60]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[320,59],[300,54],[290,57]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[290,57],[286,50],[288,43]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[287,57],[283,50],[285,43]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[288,43],[285,43]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[290,60],[275,60],[260,70]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[287,57],[275,57],[260,67]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[260,70],[260,67]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[323,62],[325,61],[330,63]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[320,59],[325,58],[330,60]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[330,60],[330,50],[330,40]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[333,60],[333,50],[333,40]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[330,40],[333,40]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[333,60],[336,60],[340,60]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[330,63],[336,63],[340,63]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[343,63],[358,56],[370,57]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[340,60],[358,53],[370,54]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[370,54],[370,50],[370,42]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[373,54],[373,50],[373,42]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[373,42],[370,42]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[370,57],[390,56],[410,57]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[373,54],[390,53],[410,54]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[410,54],[410,48],[410,42]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[413,54],[413,48],[413,42]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	#qui va la casa

	street = MAP(BEZIERCURVE([[413,42],[410,42]]))(INTERVALS(1)(32))
	streets.append(street)

	street = MAP(BEZIERCURVE([[410,57],[423,56],[447,57]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[413,54],[423,53],[447,54]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[447,57],[447,54]]))(INTERVALS(1)(32))
	streets.append(street)

	return streets


def street2(streets):
	"""
	street2 inserisce un insieme di strade

	@param streets: lista delle strade di partenza
	@return streets: lista finale delle strade
	"""

	street = MAP(BEZIERCURVE([[0,106],[40,120],[80,112]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[0,109],[40,123],[80,115]]))(INTERVALS(1)(32))
	street3 = MAP(BEZIERCURVE([[0,106],[0,109]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	streets.append(street3)

	street = MAP(BEZIERCURVE([[80,112],[160,115],[223,100]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[80,115],[160,118],[223,103]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[223,103],[226,103]]))(INTERVALS(1)(32))
	streets.append(street)

	return streets


def street1(streets):
	"""
	street1 inserisce un insieme di strade

	@param streets: lista delle strade di partenza
	@return streets: lista finale delle strade
	"""

	street = MAP(BEZIERCURVE([[0,10],[10,10],[20,5]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[0,13],[10,13],[20,8]]))(INTERVALS(1)(32))
	street3 = MAP(BEZIERCURVE([[0,10],[0,13]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)
	streets.append(street3)

	street = MAP(BEZIERCURVE([[20,5],[30,1],[40,2]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[20,8],[30,4],[40,5]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[40,2],[50,3],[60,6]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[40,5],[50,6],[60,9]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[60,6],[70,9],[80,13]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[60,9],[70,12],[80,16]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[80,13],[90,17],[100,22]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[80,16],[90,20],[100,25]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[100,22],[110,27],[120,31]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[100,25],[110,30],[120,34]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[120,31],[130,36],[150,40]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[120,34],[130,39],[150,43]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[150,40],[210,40],[223,76]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[150,43],[207,43],[220,76]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	street = MAP(BEZIERCURVE([[223,76],[225,80],[226,100]]))(INTERVALS(1)(32))
	street2 = MAP(BEZIERCURVE([[220,76],[222,80],[223,100]]))(INTERVALS(1)(32))
	streets.append(street)
	streets.append(street2)

	return streets

def insertHouse(dx,dy,dz):
	"""
	insertHouse inserisce una casa in base alle coordinate dx dy dz

	@param dx,dy,dz: valori che identificano la posizione della casa
	@return house: la casa nella posizione desiderata
	"""
	house = houseMain.multistorey_house(2)(4)(3)(2)(PI/4)
	house = T([1,2,3])([dx,dy,dz])(house)

	return house

def insertTree(dx,dy,dz):
	"""
	insertTree inserisce un albero in base alle coordinate dx dy dz

	@param dx,dy,dz: valori che identificano la posizione dell'albero
	@return tree: l'albero nella posizione
	"""
	tree = createTree()
	tree = T([1,2,3])([dx,dy,dz])(tree)

	return tree

def createTree():
	"""
	createTree ritorna l'HPC di un albero
	@return final: l'HPC dell'albero
	"""
	tree = CYLINDER([0.4,5.0])(32)
	tree = MATERIAL([0.2,0.09,0,0.4,  0,0,0,1,  0,0,0,.1, 0,0,0,1, 1])(tree)
	treeup = SPHERE(2)([100,100])
	treeup = T([3])([6])(treeup)
	treeup2 = T([2,3])([0.7,6])(SPHERE(2)([100,100]))
	treeup3 = T([2,3])([-0.7,6])(SPHERE(2)([100,100]))
	treeup4 = T([1,3])([0.7,6])(SPHERE(2)([100,100]))
	treeup5 = T([1,3])([-0.7,6])(SPHERE(2)([100,100]))
	treeup6 = T([3])([6.5])(SPHERE(2)([100,100]))
	leaf = STRUCT([treeup,treeup2,treeup3,treeup4,treeup5,treeup6])
	leaf = MATERIAL([0,0.01,0,1,  0,0.01,0,1,  0,0.1,0,1, 0,0,0,1, 0])(leaf)
	final = STRUCT([tree,leaf])
	return final

def insertTrees():
	"""
	insertTrees ritorna l'HPC di un insieme di alberi
	@return trees: l'HPC degli alberi
	"""
	trees = []
	#in basso a sinistra
	dx=20
	dy=20
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-8
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)

	dx=23
	dy=35
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-8
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)


	dx=26
	dy=54
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-8
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)



	#al centro in mezzo alle case
	dx=350
	dy=62
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-8
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)


	dx=400
	dy=62
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-8
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)

	#al centro in mezzo alle case
	dx=260
	dy=76
	up = 1
	for i in range(10):
		dx = dx+4
		if(up==1):
			dy = dy+8
			up = 0
		else:
			dy = dy-10
			up = 1
		tree = insertTree(dx,dy,3)
		trees.append(tree)

	trees = STRUCT(trees)
	return trees


def suburban_neighborhood():
	"""
	suburban_neighborhood ritorna l'HPC di un piccolo modellino di un quartiere di periferia
	@return suburban: l'HPC del quartiere
	"""

	piano = CUBOID([540,180,3])
	piano = MATERIAL([0,0.2,0,1,  0,0.2,0,1,  0,0.1,0,1, 0,0,0,1, 0])(piano)

	streets = []
	streets = street1(streets)
	streets = street2(streets)

	streets = street3(streets)
	streets = street4(streets)

	streets = STRUCT(streets)

	house1 = insertHouse(265,10,3)
	house2 = insertHouse(310,10,3)
	house3 = insertHouse(355,10,3)
	house4 = insertHouse(400,10,3)

	house5 = insertHouse(275,117,3)
	house6 = insertHouse(319,93,3)
	house7 = insertHouse(357,85,3)
	house8 = insertHouse(397,84,3)

	house9 = insertHouse(225.5,52,3)

	houses = STRUCT([house1,house2,house3,house4,house5,house6,house7,house8,house9])

	trees = insertTrees()

	streets = SOLIDIFY(streets)
	streets = T([3])([3])(streets)
	#streets = TEXTURE("texture/streets.jpg")(streets)
	#streets = MATERIAL([0.1,0.1,0.1,0.1, 0,0,0,1, 0,0,0,1, 0,0,0,1, 0])(streets)
	streets = COLOR(Color4f([64/255., 64/255., 64/255., 1]))(streets)

	suburban = STRUCT([piano,houses,trees,streets])
	return suburban

VIEW(suburban_neighborhood())

