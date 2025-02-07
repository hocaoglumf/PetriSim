from PetriNets import Petri, PetriCoordinator
import RandomValueGeneration
#import PetriNets

transitionDurationCalculation ={"t0":"RandomValueGeneration.RandomValueCalculation.Exponential(0.3)", "t1":-1,"t2":"RandomValueGeneration.RandomValueCalculation.Uniform(5,2)"}
eventGuards={"t0":"null", "t1":"null", "t2":"null"}
#state=[1,0,0,1,0]
state={"P0":1, "P1":0,"P2":0, "P3":1, "P4":0}

#eventPriority={"t0":1, "t1":1, "t2":1}
eventPriority={"t0":1, "t1":1, "t2":1}
transitionMatrix0=[[1,0,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0]]

transitionMatrix1=[[-1, 1, 0, 0,0],
                   [ 0,-1,-1, 1,0],
                   [ 0, 0, 1,-1,1]]

pn= Petri.PetriNet()
pn.SetGuards(eventGuards)
pn.SetState(state)
pn.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pn.SetTransitionDurationCalculation(transitionDurationCalculation)
pn.SetSimulationDuration(5000)
#pn.SetTransitionDuration(transitionDuration)
pn.SetEventPriority(eventPriority)
pn.SetSimulationName("Single Server ")
#pn.Simulate()


pc= PetriCoordinator.PetriCoordinator()

pc.Join(pn)
pc.Run()