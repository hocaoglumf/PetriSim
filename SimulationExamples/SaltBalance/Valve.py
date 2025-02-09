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
        transitionGuards = {"turningOn": "null", "t0": "null", "turningOff":"null"}
        timeGrantFunctions={"turningOn": "null", "t0": "null", "turningOff":"null"}
        exitFunctions={"turningOn": "null", "t0": "null", "turningOff":"null"}

        state0 = {"On": 1, "Off": 0, "OutPort0": 0, "OutPort1": 0,"SetFlowRate":1}
        #eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        eventPriority = {"turningOn": 1, "t0": 1, "turningOff":1}
        transitionMatrix0 = [[-1, 1, 1, 0, 0],
                             [1, -1, 1, 1, -1],
                             [0, [-1,1], 0, 1, 0]]

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix0)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)

        self.factoryRef = self#globals()['Ball']()
