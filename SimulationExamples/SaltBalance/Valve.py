import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Valve(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
    def Initialize(self):
        transitionGuards = {"t0": "null", "t1": "null", "t2":"isFreeFall", "t3":"isBouncing", "t4":"null", "t5":"Stop"}
        timeGrantFunctions={"t0": "null", "t1": "null", "t2":"null", "t3":"null", "t4":"null", "t5":"null"}
        exitFunctions={"t0": "null", "t1": "FreeFall", "t2":"null", "t3":"null", "t4":"Bouncing", "t5":"null"}

        state0 = {"P0": 1, "P1": 1, "P2": 0, "P3": 0,"P4":0, "P5":0}
        #eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        eventPriority = {"t0": 1, "t2": 1,"t3":1, "t5":2}
        transitionMatrix0 = [[-1, -1, 1, 0, 0, 0],
                             [ 0,  0,-1, 1, 0, 0],
                             [ 1,1,0,-1,0,0],
                             [0,0,0,-1,1,0],
                             [1,1,0,0,-1,0],
                             [0,0,0,-1,0,1]]

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix0, transitionMatrix1)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)

        self.factoryRef = self#globals()['Ball']()
