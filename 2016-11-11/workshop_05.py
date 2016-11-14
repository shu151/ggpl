from pyplasm import *
import math

def createDesk(dx, dy, dz):
	"""
	la funzione crea un tavolo in base alle dimensioni in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC del tavolo

	"""
	desk = []
	box = SKEL_1(CUBOID([5.0,5.0,3.5]))

	radius = dy/30.0

	xPlane = QUOTE([dx])
	yPlane = QUOTE([dy])
	xyPlane = PROD([xPlane, yPlane])
	xyzPlane = PROD([xyPlane, QUOTE([0.01])])

	gamba = CYLINDER([radius,dz-0.01])(30)

	desk.append(T([1])([radius*2]))
	desk.append(T([2])([radius*2]))

	desk.append(gamba)
	desk.append(T([2])([dy-radius*4]))

	desk.append(gamba)
	desk.append(T([1])([dx-radius*4]))

	desk.append(gamba)
	desk.append(T([2])([-dy+radius*4]))
	desk.append(gamba)

	desk.append(T([1,2,3])([-dx+radius*2,-radius*2,dz-0.01]))
	xyzBeam = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzPlane)
	desk.append(xyzBeam)

	return desk


def createChair(dx, dy, dz):
	"""
	la funzione crea una sedia in base alle dimensioni in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC della sedia

	"""

	radius = dy/30.0
	chair = createDesk(dx,dy,dz/2)
	gamba = CYLINDER([radius,(dz/2)])(30)

	chair.append(T([3])([0.01]))
	chair.append(T([1])([radius*2]))
	chair.append(T([2])([radius*2]))
	chair.append(gamba)
	chair.append(T([1])([dx-radius*4]))
	chair.append(gamba)
	
	xBeam = QUOTE([dx])
	yBeam = QUOTE([0.01])
	xyBeam = PROD([xBeam, yBeam])
	xyzBeam = PROD([xyBeam, QUOTE([dy/3+0.05])])

	chair.append(T([1,2,3])([-dx+radius*2,radius,0.13]))
	xyzBeam = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBeam)
	chair.append(xyzBeam)

	return chair

def createTeachingPost(dx,dy,dz):
	"""
	la funzione crea una cattedra in base alle dimensioni in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC della cattedra

	"""
	teachingPost = []

	#box = SKEL_1(CUBOID([dx,dy,dz]))
	#teachingPost.append(box)

	xPlane = QUOTE([dx])
	yPlane = QUOTE([dy])
	xyPlane = PROD([xPlane, yPlane])
	xyzPlane = PROD([xyPlane, QUOTE([dz/80.0])])
	xyzPlane = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzPlane)
	teachingPost.append(T([3])(dz-dz/80.0))
	teachingPost.append(xyzPlane)

	teachingPost.append(T([3])(-(dz-dz/80.0)))

	xyBack = PROD([QUOTE([dx]), QUOTE([dy/80.0])])
	xyzBack = PROD([xyBack, QUOTE([dz-dz/80.0])])
	xyzBack = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBack)
	teachingPost.append(T([2])(dy/60.0))
	teachingPost.append(xyzBack)

	teachingPost.append(T([2])(dy/80.0))

	xySide = PROD([QUOTE([dx/60.0]), QUOTE([dy-dy/60.0-dy/80.0])])
	xyzSide = PROD([xySide, QUOTE([dz-dz/80.0])])
	xyzSide = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzSide)
	teachingPost.append(T([1])(dx/70.0))
	teachingPost.append(xyzSide)
	teachingPost.append(T([1])(dx-dx/60.0-(dx/70.0)*2))
	teachingPost.append(xyzSide)

	teachingPost.append(T([1])(-dx+dx/60.0*2+(dx/70.0)*2))

	xyDrawers = PROD([QUOTE([dx/2.0]), QUOTE([dy/2.0])])
	xyzDrawers = PROD([xyDrawers, QUOTE([dz/5.0])])
	xyzDrawers = (COLOR(Color4f([110/255.,93/255.,64/255.,1])))(SKEL_2(xyzDrawers))
	teachingPost.append(T([3])(dz-dz/80.0-dz/5.0))
	teachingPost.append(T([2])(-dy/80.0-dy/60.0+dy-dy/2.0-dy/70.0))
	teachingPost.append(xyzDrawers)

	knob = SPHERE(dz/40.0)([100,100])
	knob = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(knob)
	teachingPost.append(T([3])(dz/5.0/2.0))
	teachingPost.append(T([2])(dy/2.0+dz/40.0))
	teachingPost.append(T([1])(dx/4.0))
	teachingPost.append(knob)

	return STRUCT(teachingPost)


def createCloset(dx,dy,dz):
	"""
	la funzione crea un armadio in base alle dimensioni in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC dell'armardio

	"""
	closet = []
	#box = SKEL_1(CUBOID([dx,dy,dz]))
	#closet.append(box)
	xyPlane = PROD([QUOTE([dx]), QUOTE([dy])])
	xyzPlane = PROD([xyPlane, QUOTE([dz/60.0])])
	xyzPlane = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzPlane)

	closet.append(xyzPlane)

	closet.append(T([3])(dz/60.0))
	closet.append(T([2])(dy/60.0))

	xyBack = PROD([QUOTE([dx]), QUOTE([dy/50.0])])
	xyzBack = PROD([xyBack, QUOTE([dz-dz/60.0-dz/60.0])])
	xyzBack = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBack)
	closet.append(xyzBack)

	xySide = PROD([QUOTE([dx/60.0]), QUOTE([dy-dy/60.0-dy/50.0])])
	xyzSide = PROD([xySide, QUOTE([dz-dz/60.0-dz/60.0])])
	xyzSide = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzSide)
	closet.append(T([2])(dy/50.0))
	closet.append(xyzSide)
	closet.append(T([1])(dx-dx/60.0))
	closet.append(xyzSide)
	closet.append(T([1])(-dx+dx/60.0))
	closet.append(T([2])(-dy/50.0-dy/60.0))
	closet.append(T([3])(dz-dz/60.0-dz/60.0))
	closet.append(xyzPlane)

	xyClosetDoor = PROD([QUOTE([(dx-dx/60.0*2)/2]), QUOTE([dy/50.0])])
	xyzClosetDoor = PROD([xyClosetDoor, QUOTE([dz-dz/60.0-dz/60.0])])
	xyzClosetDoor = (COLOR(Color4f([0/255.,0/255.,0/255.,1])))(xyzClosetDoor)

	closet.append(T([1])(dx/60.0))
	closet.append(T([3])(-dz+dz/60.0+dz/60.0))
	closet.append(T([2])(dy-dy/50))

	knob = SPHERE(dz/70.0)([100,100])
	knob = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(knob)

	closet.append(R([1,2])(PI/4)(xyzClosetDoor))
	closet.append(T([1])((dx-dx/60.0*2)/2))
	closet.append(xyzClosetDoor)

	closet.append(T([1,2,3])([dx/20.0,dz/70.0,dz/2]))
	closet.append(knob)

	return STRUCT(closet)


def createRoom(dx,dy,dz):
	"""
	la funzione crea una stanza all'interno dei valori in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC della stanza

	"""

	desk = STRUCT(createDesk(1.0,0.5,0.6))
	chair = STRUCT(createChair(0.45,0.4,0.7))
	teachingPost = createTeachingPost(1.0,0.6,0.8)
	closet = createCloset(1.0,0.6,1.5)
	blackboard = createBlackboard(1.5,0.4,2.0)

	base = PROD([QUOTE([dx]), QUOTE([dy])])
	base = (COLOR(Color4f([128/255.,128/255.,128/255.,1])))(base)
	room = STRUCT([base])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),T([2])(-0.3),T([1])(0.275),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),T([2])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),T([2])(1.5-0.3),T([1])(0.275),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),T([2])(3),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk,T([1])(1.5),desk])
	room = STRUCT([room,T([1])(1.5),T([2])(1.5),T([2])(3-0.3),T([1])(0.275),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair,T([1])(1.5),chair])

	room = STRUCT([room,T([1])(4.5),T([2])(7),teachingPost])
	room = STRUCT([room,T([1])(5.2),T([2])(8),R([1,2])(PI)(chair)])
	room = STRUCT([room,T([1])(dx-1.3),closet])
	room = STRUCT([room,T([1])(2),T([2])(7),blackboard])

	return room

def createBlackboard(dx,dy,dz):
	"""
	la funzione crea una lavagna in base alle dimensioni in input

	@param dx: valore asse x
	@param dy: valore asse y
	@param dz: valore asse z
	@return closet: un modello HPC della lavagna

	"""

	xyBase = PROD([QUOTE([dx/20.0]), QUOTE([dy])])
	xyzBase = PROD([xyBase, QUOTE([dz/60.0])])
	xyzBase = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBase)

	#blackboard = STRUCT([SKEL_1(CUBOID([dx,dy,dz])),xyzBase])
	blackboard = STRUCT([xyzBase])
	blackboard = STRUCT([blackboard,T([1])(dx-dx/20.0),xyzBase])

	xyPillar = PROD([QUOTE([dx/20.0]), QUOTE([dy/7.0])])
	xyzPillar = PROD([xyPillar, QUOTE([dz-dz/4.0])])
	xyzPillar = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzPillar)

	blackboard = STRUCT([blackboard,T([2])(dy/2.0-(dy/7.0)/2.0),T([3])(dz/60.0),xyzPillar,T([1])(dx-dx/20.0),xyzPillar])

	xyBoard = PROD([QUOTE([dx-dx/20.0-dx/20.0-0.02]), QUOTE([dy/7])])
	xyzBoard = PROD([xyBoard, QUOTE([dz/2.5])])
	xyzBoard = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBoard)
	xyBlack = PROD([QUOTE([dx-dx/20.0-dx/20.0-0.02-dx/20.0]), QUOTE([dy/7])])
	xyzBlack = PROD([xyBlack, QUOTE([dz/2.5-dz/30.0])])
	xyzBlack = (COLOR(Color4f([0/255.,0/255.,0/255.,1])))(xyzBlack)
	xyzBlack = STRUCT([T([1])(dx/20.0/2),T([3])(dz/30.0/2),xyzBlack])
	diff = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(DIFFERENCE([xyzBoard,xyzBlack]))
	blackboardPiece = STRUCT([diff,xyzBlack])
	blackboardPiece = R([2,3])(PI/4)(blackboardPiece)

	spostamento = dz/2.5*math.cos(PI/4.0)/2

	blackboard = STRUCT([blackboard,T([1])(dx/20.0+0.01),T([2])(dy/2.0-(dy/7.0)/2.0),T([3])(dz/60.0+dz-dz/4.0-dz/2.5),T([2])(spostamento),blackboardPiece])

	xyBeam = PROD([QUOTE([dx-dx/20.0-dx/20.0]), QUOTE([dy/7])])
	xyzBeam = PROD([xyBeam, QUOTE([dz/60.0])])
	xyzBeam = (COLOR(Color4f([220/255.,165/255.,116/255.,1])))(xyzBeam)

	blackboard = STRUCT([blackboard,T([1])(dx/20.0),T([2])(dy/2.0-(dy/7.0)/2.0),T([3])(dz/60.0+dz-dz/4.0-dz/2.5-dz/60.0-dz/60.0),xyzBeam])

	return blackboard



VIEW(STRUCT(createDesk(1.0,0.5,0.6)))
VIEW(STRUCT(createChair(0.45,0.4,0.7)))
VIEW(createTeachingPost(1.0,0.6,0.8))
VIEW(createCloset(1.0,0.6,1.5))
VIEW(createBlackboard(1.5,0.4,2.0))
VIEW(createRoom(10,8.5,4))
