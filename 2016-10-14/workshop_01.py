from pyplasm import*

def struttura():

	#stringa = raw_input()
	#inputList = string.split()
	#dis = [float(x) for x in inputList]
	a = 3
	b = 4
	c = 5

	d = 1
	i = 2

	e = 3
	f = 4
	g = 2 #deve essere uguale a l

	h = 0.5
	l = 2

	#variabili
	distanzaTraPilastri = [a,b,c]
	grandezzaPilastro = (d,i)

	distanzaTraBasi = [e,f,g]
	grandezzaBase = (h,l)


	

	listaPilastri = []
	for dist in distanzaTraPilastri:
		listaPilastri.append(d)
		listaPilastri.append(dist-dist*2)
	listaPilastri.append(d)

	sommaDistanzePilastri = sum([abs(i) for i in distanzaTraPilastri])




	listaBasi = []
	for dist in distanzaTraBasi:
		listaBasi.append(dist)
		listaBasi.append(-h)
	listaBasi.append(-h)

	sommaDistanzeBasi = sum([abs(i) for i in distanzaTraBasi])
	print(listaBasi)

	listaBasi2 = []
	for dist in distanzaTraBasi:
		listaBasi2.append(dist-dist*2)
		listaBasi2.append(h)


	x = QUOTE(listaPilastri)
	y = QUOTE([grandezzaPilastro[1]])
	xy = PROD([x,y])
	xyz = PROD([xy, QUOTE(listaBasi)])

	xbase = QUOTE([sommaDistanzePilastri+len(distanzaTraPilastri)+1])
	ybase = QUOTE([grandezzaBase[1]])
	xybase = PROD([xbase, ybase])
	xyzbase = PROD([xybase, QUOTE(listaBasi2)])


	VIEW(STRUCT([xyz, xyzbase]))


struttura()