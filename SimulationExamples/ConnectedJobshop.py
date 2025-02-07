from PetriNets import Petri, PetriCoordinator
'''Generator'''


transitionDurationCalculation ={"t0":"RandomValueCalculation.Exponential(1.3)"}
eventGuards={"t0":"null"}
state={"P0":1,"P1":0}

eventPriority={"t0":1}
transitionMatrix0=[[1, 1]]
transitionMatrix1=[[-1, 0]]
pg= Petri.PetriNet()
pg.SetGuards(eventGuards)
pg.SetTransitionDurationCalculation(transitionDurationCalculation)
pg.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pg.SetState(state)
#pg.SetSimulationDuration(5000)
#pn.SetTransitionDuration(transitionDuration)
pg.SetEventPriority(eventPriority)
pg.SetSimulationName("Generator ")

''' Machine -0'''

''' Common data '''
eventGuards={"t0":"null", "t1":"null"}
state0={"P0":0,"P1":1,"P2":0,"P3":0}

eventPriority={"t0":1,"t1":1}
transitionMatrix0=[[-1,-1,1,0],
                   [0,1,-1,1]]
transitionMatrix1=[[0,0,0,0],
                   [0,0,0,0]]
''' Machine-0 private data '''
transitionDurationCalculation ={"t0":-1, "t1":1}
''' Machine-1 private data '''
transitionDurationCalculation1 ={"t0":-1, "t1":3}

pm0= Petri.PetriNet()
pm0.SetGuards(eventGuards)
pm0.SetTransitionDurationCalculation(transitionDurationCalculation)
pm0.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pm0.SetState(state0)
#pm0.SetSimulationDuration(5000)
#pn.SetTransitionDuration(transitionDuration)
pm0.SetEventPriority(eventPriority)
pm0.SetSimulationName("Makine0 ")


pm1= Petri.PetriNet()
pm1.SetGuards(eventGuards)
pm1.SetTransitionDurationCalculation(transitionDurationCalculation1)
pm1.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
state1={"P0":0,"P1":1,"P2":0,"P3":0}

pm1.SetState(state1)
#pm1.SetSimulationDuration(5000)
#pn.SetTransitionDuration(transitionDuration)
pm1.SetEventPriority(eventPriority)
pm1.SetSimulationName("Makine1 ")


pc= PetriCoordinator.PetriCoordinator()
pc.AttachTransition([pg,"P1",1,pm0, "P0", 1])
pc.AttachTransition([pm0,"P3", 10, pm1, "P0",10 ])
pc.Join(pg)
pc.Join(pm0)
pc.Join(pm1)
pc.SetChat(True)
pc.SetExecutionDuration(50000)
pc.Run()