import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Consumer(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
        self.N=5
    def Initialize(self):
        transitionGuards = {"t0": "null","t1": "null","t2": "null","t3": "null"}
        timeGrantFunctions={"t0": "null","t1": "null","t2": "null","t3": "null"}
        exitFunctions={"t0": "null","t1": "null","t2": "null","t3": "null"}

        state0 = {"inPort":0,"P0": 1, "P1": 0, "P2":0, "P3":0, "outPort":0}

        eventPriority = {"t0": 1,"t1": 1,"t2": 1,"t3": 1}
        transitionMatrix = [[ 0, 1, 0,-1, 0, 0],
                            [-1,-1, 1, 0, 0, 0],
                            [ 0, 1,-1, 0, 1, 1],
                            [ 0,-1, 0, 1,"Meth:BreakerNumber:-1", 0]]

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)
        self.SetTransitionStates({"t0": 0, "t1": 0, "t2": 0, "t3": 0})  # There is no transition that is external transition allowed

        self.factoryRef = self

    def BreakerNumber(self):
        y=self.coordinator.GetMinNumberofToken("Consumer","P2")
        p3=self.GetTokenNumber("P3")
        s=p3+y
        rr=max([s,self.N])
        return rr
