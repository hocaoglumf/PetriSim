import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Generator(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
    def Initialize(self):
        transitionGuards = {"t4": "null"}
        timeGrantFunctions={"t4": "null"}
        exitFunctions={"t4": "null"}

        state0 = {"P4": 1, "P5": 0}
        #eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        eventPriority = {"t4": 1}
        transitionMatrix = [[[-1,1],1]]

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)

        self.factoryRef = self
