from pyplasm import *

def ggpl_doors_and_windows():

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


	XDoor = [.1,.2,0.05,.2,.1,.1,.2,0.05,.2,.1]
	YDoor = [0.7,.1,.3,.05,.35,.05,0.3,0.1]
	ZDoor = [0.0,3.0,8.0,10.0]
	occupancyDoor = [[True, True, True, True, True, True, True, True],
			  [True, True, False, True, False, True, False, True],
			  [True, True, True, True, True, True, True, True],
			  [True, True, False, True, False, True, False, True],
			  [True, True, True, True, True, True, True, True],
			  [True, True, True, True, True, True, True, True],
			  [True, True, False, True, False, True, False, True],
			  [True, True, True, True, True, True, True, True],
			  [True, True, False, True, False, True, False, True],
			  [True, True, True, True, True, True, True, True]]

	def createDoor(X,Y,Z,occupancy,dx,dy,dz):
		"""
		createDoor genera un modello HPC di una porta
		@param X: lista di Float che indicano gli intervalli di celle da analizzare (asse x)
		@param Y: lista di Float che indicano gli intervalli di celle da analizzare (asse y)
		@param Z: nulla, da implementare
		@param occupancy: True se la cella occupancy[X[i],Y[j]] e' piena, False altrimenti (vuota)
		@param dx: valore asse x del box che deve contenere la porta
		@param dy: valore asse y del box che deve contenere la porta
		@param dz: valore asse z del box che deve contenere la porta
		@return result: modello HPC della porta
		"""

		sumX= sum(X) #utilizzati per inserirlo all'interno del box dx dy dz (per parametrizzarlo)
		sumY= sum(Y)
		door = []
		sumValuesX = 0
		for i in range(len(X)):
			yQuote = []
			for y in range(len(Y)):
				if(occupancy[i][y] == True):
					yQuote.append(Y[y]/sumY*dz)
				else:
					yQuote.append(-Y[y]/sumY*dz)
			door.append(PROD([QUOTE([-sumValuesX/sumX*dx, X[i]/sumX*dx]), QUOTE(yQuote)]))
			sumValuesX = sumValuesX + X[i]
		result = STRUCT(door)
		result = PROD([result, Q(dy)])
		result = MAP([S1,S3,S2])(result)
		knob = SPHERE(dz/70.0)([100,100])
		knob = COLOR(Color4f([217/255., 138/255., 95/255., 1]))(knob)
		result = COLOR(Color4f([217/255., 138/255., 95/255., 1]))(result)
		result = STRUCT([result,T([2])(dy+dz/70.0),T([1])(dx/2-dx/2/20),T([3])(dz/2),knob])
		return result


	def createWindow(X,Y,Z,occupancy,dx,dy,dz):
		"""
		createWindow genera un modello HPC di una finestra
		@param X: lista di Float che indicano gli intervalli di celle da analizzare (asse x)
		@param Y: lista di Float che indicano gli intervalli di celle da analizzare (asse y)
		@param Z: nulla, da implementare
		@param occupancy: True se la cella occupancy[X[i],Y[j]] e' piena, False altrimenti (vuota)
		@param dx: valore asse x del box che deve contenere la finestra
		@param dy: valore asse y del box che deve contenere la finestra
		@param dz: valore asse z del box che deve contenere la finestra
		@return result: modello HPC della finestra
		"""

		sumX= sum(X)
		sumY= sum(Y)
		window = []
		sumValuesX = 0
		for i in range(len(X)):
			yQuote = []
			for y in range(len(Y)):
				if(occupancy[i][y] == True):
					yQuote.append(Y[y]/sumY*dz)
				else:
					yQuote.append(-Y[y]/sumY*dz)
			window.append(PROD([QUOTE([-sumValuesX/sumX*dx, X[i]/sumX*dx]), QUOTE(yQuote)]))
			sumValuesX = sumValuesX + X[i]
		result = STRUCT(window)
		result = PROD([result, Q(dy)])
		result = MAP([S1,S3,S2])(result)
		knob = SPHERE(dz/70.0)([100,100])
		knob = COLOR(Color4f([217/255., 138/255., 95/255., 1]))(knob)
		result = COLOR(Color4f([217/255., 138/255., 95/255., 1]))(result)
		result = STRUCT([result,T([2])(dy+dz/70.0),T([1])(dx/2-dx/2/20),T([3])(dz/2),knob])
		return result


	VIEW(createWindow(X,Y,Z,occupancy,2.,0.15,2.))

	VIEW(createDoor(XDoor,YDoor,ZDoor,occupancyDoor,2.,0.15,3.))

ggpl_doors_and_windows()