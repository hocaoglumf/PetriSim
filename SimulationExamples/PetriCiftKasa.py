from PetriNets import Petri, PetriCoordinator

transitionMatrix0=[
[1,0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	]]

transitionMatrix1=[
[-1, 1,	0,	0,	0,	0,	0	],
[0,	-1,	-1,	1,	0,	0,	0	],
[0,	-1,	0,	0,	0,	-1,	1	],
[0,	0,	1,	-1,	1,	0,	0	],
[0,	0,	0,	0,	1,	1,	-1	]]

transitionDurationCalculation ={"e0":3, "e1":-1,"e2":-1, "e3":5,"e4":6}
state={"P0":1, "P1":0, "P2":1, "P3":0, "P4":0, "P5":1,"P6":0}#[1,0,1,0,0,1,0]

#eventPriority={"e0":1, "e1":1, "e2":2,"e3":1, "e4":1}
eventPriority={"e0":Petri.Event(1), "e1":Petri.Event(1), "e2":Petri.Event(2),"e3":Petri.Event(1), "e4":Petri.Event(1)}


pn= Petri.PetriNet()
pn.SetTransitionDurationCalculation(transitionDurationCalculation)
pn.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pn.SetState(state)
#pn.SetSimulationDuration(15000)
pn.SetEventPriority(eventPriority)
pn.SetSimulationName("Çift Kasa ")
#pn.Simulate()

pc= PetriCoordinator.PetriCoordinator()

pc.Join(pn)
pc.Run()
