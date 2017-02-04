from pyplasm import *
from scipy import *  
from numpy import *  
import math

def ggpl_roof(verts,angolo,altezzaFalda,direzioni):
	"""
	ggpl_roof ritorna l'HPC di un tetto secondo 4 parametri: i vertici del contorno del tetto, i gradi della pendenza delle falde, 
	la lunghezza della pendenza delle falde e la direzione di ogni falda 
	@param verts: lista delle coordinate xyz dei vertici (devono essere ordinati secondo punti adiacenti)
	@param angolo: l'angolo di inclinazione che si vuole dare alla falda
	@param altezzaFalda: lunghezza della pendenza della falda
	@param direzione: indica in quale quadrante (di un ipotetico piano cartesiano) 1,2,3 o 4 va direzionata la falda
	@return struttura: l'HPC del tetto
	"""

	falde = []
	for i in range(len(direzioni)):
		if i==len(direzioni)-1:
			falde.append(creaFalda(verts[i],verts[0],angolo,altezzaFalda,direzioni[i]))
		else:
			s = i+1
			falde.append(creaFalda(verts[i],verts[s],angolo,altezzaFalda,direzioni[i]))


	rette = []
	for i in range(len(falde)):
		rette.append(equazioneRettaPerDuePunti(falde[i][2],falde[i][3]))

	intersezioni = []
	for i in range(len(rette)):
		if i==len(rette)-1:
			intersezioni.append(intersezioneDueRette(rette[i],rette[0]))
		else:
			s = i+1
			intersezioni.append(intersezioneDueRette(rette[i],rette[s]))

	faldeFinali = []
	for i in range(len(direzioni)):
		if i == 0:
			f = MKPOL([[[falde[i][0][0],falde[i][0][1],0],[falde[i][1][0],falde[i][1][1],0],[intersezioni[i][0],intersezioni[i][1],falde[1][2][2]],[intersezioni[len(direzioni)-1][0],intersezioni[len(direzioni)-1][1],falde[0][2][2]]],[[1,2,3,4]],None])
			f = TEXTURE("roofing.jpg")(f)
			faldeFinali.append(f)
		else:
			f = MKPOL([[[falde[i][0][0],falde[i][0][1],0],[falde[i][1][0],falde[i][1][1],0],[intersezioni[i][0],intersezioni[i][1],falde[1][2][2]],[intersezioni[i-1][0],intersezioni[i-1][1],falde[0][2][2]]],[[1,2,3,4]],None])
			f = TEXTURE("roofing.jpg")(f)
			faldeFinali.append(f)

	vertsContorno = [[] for _ in range(len(intersezioni)+1)]
	cella = []
	for i in range (len(intersezioni)):
		vertsContorno[i].append(intersezioni[i][0])
		vertsContorno[i].append(intersezioni[i][1])
		s = i+1
		if i==len(intersezioni)-1:
			vertsContorno[s].append(intersezioni[0][0])
			vertsContorno[s].append(intersezioni[0][1])
		cella.append(s)


	contorno = POLYLINE(vertsContorno)
	contorno = SOLIDIFY(contorno)

	terrazzo = T(3)(falde[0][2][2])(contorno)
	terrazzo = TEXTURE("roofing2.jpg")(terrazzo)

	tetto = STRUCT(faldeFinali)
	return STRUCT([terrazzo,tetto])

def ggpl_roofDiProva(verts,angolo,altezzaFalda,direzioni):
	"""
	funzione solo di prova non usare
	ggpl_roofDiProva ritorna l'HPC di un tetto secondo 4 parametri: i vertici del contorno del tetto, i gradi della pendenza delle falde, 
	la lunghezza della pendenza delle falde e la direzione di ogni falda 
	@return struttura: l'HPC del tetto
	"""

	#verts = [[0,0,0],[5,1,0],[4,3,0],[2,3,0]]
	#verts = [[2,1,0],[1,3,0],[2,5,0],[4,3,0]]
	pianta = MKPOL([verts,[[1,2,3,4]],None])
	#angolo = PI/4
	#altezzaFalda = 1
	vert1 = verts[0]
	vert2 = verts[1]
	vert3 = verts[2]
	vert4 = verts[3]
	
	falda1 = creaFalda(vert1,vert2,angolo,altezzaFalda,direzioni[0])
	falda2 = creaFalda(vert2,vert3,angolo,altezzaFalda,direzioni[1])
	falda3 = creaFalda(vert3,vert4,angolo,altezzaFalda,direzioni[2])
	falda4 = creaFalda(vert4,vert1,angolo,altezzaFalda,direzioni[3])
	retta1 = equazioneRettaPerDuePunti(falda1[2],falda1[3])
	retta2 = equazioneRettaPerDuePunti(falda2[2],falda2[3])
	retta3 = equazioneRettaPerDuePunti(falda3[2],falda3[3])
	retta4 = equazioneRettaPerDuePunti(falda4[2],falda4[3])
	intersezione12 = intersezioneDueRette(retta1,retta2)
	print "int12", intersezione12
	intersezione23 = intersezioneDueRette(retta2,retta3)
	print "int23", intersezione23
	intersezione34 = intersezioneDueRette(retta3,retta4)
	intersezione41 = intersezioneDueRette(retta4,retta1)
	f1 = MKPOL([[[falda1[0][0],falda1[0][1],0],[falda1[1][0],falda1[1][1],0],[intersezione12[0],intersezione12[1],falda1[2][2]],[intersezione41[0],intersezione41[1],falda1[2][2]]],[[1,2,3,4]],None])
	f1 = TEXTURE("roofing.jpg")(f1)
	f2 = MKPOL([[[falda2[0][0],falda2[0][1],0],[falda2[1][0],falda2[1][1],0],[intersezione23[0],intersezione23[1],falda2[2][2]],[intersezione12[0],intersezione12[1],falda2[2][2]]],[[1,2,3,4]],None])
	f2 = TEXTURE("roofing.jpg")(f2)
	f3 = MKPOL([[[falda3[0][0],falda3[0][1],0],[falda3[1][0],falda3[1][1],0],[intersezione23[0],intersezione23[1],falda3[2][2]],[intersezione34[0],intersezione34[1],falda3[2][2]]],[[1,2,3,4]],None])
	f3 = TEXTURE("roofing.jpg")(f3)
	f4 = MKPOL([[[falda4[0][0],falda4[0][1],0],[falda4[1][0],falda4[1][1],0],[intersezione34[0],intersezione34[1],falda1[2][2]],[intersezione41[0],intersezione41[1],falda1[2][2]]],[[1,2,3,4]],None])
	f4 = TEXTURE("roofing.jpg")(f4)

	contorno = MKPOL([[[intersezione12[0],intersezione12[1]],[intersezione23[0],intersezione23[1]],[intersezione34[0],intersezione34[1]],[intersezione41[0],intersezione41[1]]],[[1,2,3,4]],None])

	terrazzo = T(3)(falda1[2][2])(contorno)
	terrazzo = TEXTURE("roofing2.jpg")(terrazzo)

	contorno = SKEL_1(contorno)

	pianta = SKEL_1(pianta)
	return STRUCT([terrazzo,pianta,f1,f2,f3,f4])
	VIEW(STRUCT([terrazzo,pianta,f1,f2,f3,f4]))
	VIEW(STRUCT([f1,f2,f3,f4]))

def creaFalda(vert1, vert2, angolo, altezzaFalda, direzione):
	"""
	creaFalda ritorna i 4 vertici della falda che e' ancora un piano rettangolare(non prevede il calcolo dei punti di giunzione con gli altri piani)
	@param vert1: lista delle coordinate xyz del vertice1
	@param vert2: lista delle coordinate xyz del vertice2
	@param angolo: l'angolo di inclinazione che si vuole dare alla falda
	@param altezzaFalda: lunghezza della pendenza della falda
	@param direzione: indica in quale quadrante (di un ipotetico piano cartesiano) 1,2,3 o 4 va direzionata la falda
	@return verts: i quattro vertici della falda
	"""
	linea = MKPOL([[vert1,vert2],[[1,2]],None])

	if vert1[1]>vert2[1]:
		x=vert1[0]
		y=vert2[1]
	else:
		x=vert2[0]
		y=vert1[1]

	vert3 = [x,y]

	#AB = sqrt[(x2- x1)^2 + (y2- y1)^2]
	distv1v2 = sqrt((vert1[0]-vert2[0])*(vert1[0]-vert2[0])+(vert1[1]-vert2[1])*(vert1[1]-vert2[1]))
	distv1v3 = sqrt((vert1[0]-vert3[0])*(vert1[0]-vert3[0])+(vert1[1]-vert3[1])*(vert1[1]-vert3[1]))
	distv2v3 = sqrt((vert2[0]-vert3[0])*(vert2[0]-vert3[0])+(vert2[1]-vert3[1])*(vert2[1]-vert3[1]))
	
	#distv2v3 = distv1v2 * math.cos(a)
	#math.cos(a) = distv2v3/distv1v2
	a = math.asin(distv2v3/distv1v2)

	b = PI/2-a

	distv2v4 = altezzaFalda * math.cos(angolo)

	altezzaPerpendicolareFalda = sqrt(altezzaFalda*altezzaFalda-distv2v4*distv2v4)
	distv2v5 = distv2v4 * math.cos(b)

	distv4v5 = sqrt(distv2v4*distv2v4-distv2v5*distv2v5)


	if direzione==1:
		vert6 = [vert2[0]+distv2v4,vert2[1]+distv4v5,altezzaPerpendicolareFalda]
		vert7 = [vert1[0]+distv2v4,vert1[1]+distv4v5,altezzaPerpendicolareFalda]
	elif direzione==2:
		vert6 = [vert2[0]-distv2v4,vert2[1]+distv4v5,altezzaPerpendicolareFalda]
		vert7 = [vert1[0]-distv2v4,vert1[1]+distv4v5,altezzaPerpendicolareFalda]
	elif direzione==3:
		vert6 = [vert2[0]-distv2v4,vert2[1]-distv4v5,altezzaPerpendicolareFalda]
		vert7 = [vert1[0]-distv2v4,vert1[1]-distv4v5,altezzaPerpendicolareFalda]
	elif direzione==4:
		vert6 = [vert2[0]+distv2v4,vert2[1]-distv4v5,altezzaPerpendicolareFalda]
		vert7 = [vert1[0]+distv2v4,vert1[1]-distv4v5,altezzaPerpendicolareFalda]

	verts = [vert1,vert2,vert6,vert7]
	prova = MKPOL([verts,[[1,2,3,4]],None])


	return verts

	linea = PROD([linea,QUOTE([2])])
	linea = R([3,2])(angolo)(linea)

	#VIEW(linea)


def equazioneRettaPerDuePunti(vert1,vert2):
	"""
	equazioneRettaPerDuePunti ritorna la retta dati come input due vertici
	@param vert1: lista delle coordinate xyz del vertice1 (z non serve)
	@param vert2: lista delle coordinate xyz del vertice2 (z non serve)
	@return retta: ritorna la retta (una lista di tre elementi) secondo il seguente schema x + y = n --> [x,y,n]
	"""

	x1=vert1[0]
	x2=vert2[0]
	y1=vert1[1]
	y2=vert2[1]
	m=0
	q=0

	# Se i due punti hanno la stessa ascissa, la retta che li comprende e' parallela all'asse y
	# Se i due punti hanno la stessa ordinata, la retta che li comprende e' parallela all'asse x
	if x1==x2:
		retta = [1,0,x1]
	elif y1==y2:
		retta = [0,1,y1]
	else:
		m=(float(y2)-float(y1))/(float(x2)-float(x1))
		q=float(y1)-m*float(x1)
		retta = [-m,1,q]

	return retta

def intersezioneDueRette(retta1,retta2):
	"""
	intersezioneDueRette ritorna il punto di intersezione di due rette
	@param retta1: e' la retta definita secondo le regole del metodo equazioneRettaPerDuePunti
	@param retta2: e' la retta definita secondo le regole del metodo equazioneRettaPerDuePunti
	@return punto: ritorna il punto x y dell'intersezione
	"""
	  
	# La matrice A contiene i coefficenti (a sinistra del simbolo di uguale).  
	A = matrix([[retta1[0], retta1[1]], [retta2[0], retta2[1]]])  
	
	# l'array b contiene i valori noti  
	b = array([retta1[2], retta2[2]])  
	  
	# la funzione linalg.solve risolve sistemi lineari
	punto = linalg.solve(A, b)  

	return punto

def equazionePianoPerTrePunti(vert1,vert2,vert3):
	"""
	equazionePianoPerTrePunti ritorna il piano dati tre vertici nello spazio
	@param vert1: lista delle coordinate xyz del vertice1
	@param vert2: lista delle coordinate xyz del vertice2
	@param vert3: lista delle coordinate xyz del vertice3
	@return piano: ritorna il piano definito come un vettore di 4 variabili [a,b,c,d]
	"""

	p1 = np.array(vert1)
	p2 = np.array(vert2)
	p3 = np.array(vert3)

	# vettori che sono nel piano
	v1 = p3 - p1
	v2 = p2 - p1
	# l'in
	# il prodotto incrociato e' un vettore normale al piano
	cp = np.cross(v1, v2)
	a, b, c = cp
	# a * x3 + b * y3 + c * z3 = d
	d = np.dot(cp, p3)
	print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))
	return [a,b,c,d]

verts = [[2,1,0],[1,3,0],[2,5,0],[4,3,0]]
#VIEW(ggpl_roofDiProva(verts,PI/4,1,[1,4,3,2]))
verts2 = [[4,1,0],[2.5,2.5,0],[5,5,0],[6,7.5,0],[11,8.5,0],[13.5,4.5,0],[13.5,2.5,0],[9,5,0]]
#VIEW(ggpl_roof(verts2,PI/4,1,[1,4,4,4,3,2,1,2]))
#verts3 = [[21.649341,86.619577],[875.5955600000001,86.619577],[875.5955600000001,86.619577],[875.5955600000001,798.6423400000001],[435.3923000000001,798.6423400000001],[435.3923000000001,798.6423400000001],[435.3923000000001,766.1683300000001],[435.3923000000001,766.1683300000001],[21.649341000000106,766.1683300000001],[21.649341,86.619577],[21.649341000000106,766.1683300000001]]
#VIEW(ggpl_roof(verts3,PI/4,1,[1,4,4,4,3,2,1,2]))