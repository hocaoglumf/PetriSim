import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Tank(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
        self.m=100
        self.vol=0

    def Initialize(self):
        transitionGuards = {"t0": "null", "T0": "null", "t1":"null"}
        timeGrantFunctions={"t0": "null", "T0": "null", "t1":"null"}
        exitFunctions={"t0": "null", "T0": "null", "t1":"null"}

        state0 = {"P0": 1, "P1": 1, "InPort0": 0, "InPort1": 0,"C0":0, "V0":0,"S0":0}
        eventPriority = {"t0": 1, "T0": 1,"t1":1}
        transitionMatrix = [[-1, 0, -1, 0, "Att:m", 0,0],
                            [0, 0, 0, 0, 0, 0,0],
                            [0, 0, 0, 0, 0, 0, 0]]

        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)

        self.factoryRef = self#globals()['Ball']()

    def SetAmount(self,a):
        self.m=a

    def FuncVol(self):
        pass

