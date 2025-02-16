import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Sir(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None

    def Initialize(self):
        self.beta=0.3
        self.gamma=0.1
        self.initialS=0.9
        self.initialI=0.3
        self.initialR=0.0

        transitionGuards = {"initial": "null", "t0": "null", "t1":"null", "t2":"null"}
        timeGrantFunctions={"initial": "null", "t0": "null", "t1":"null", "t2":"null"}
        exitFunctions={"initial": "null", "t0": "LastState", "t1":"null", "t2":"null"}

        state0 = {"P0": 1, "P1": 0, "P2": 0, "P3": 0}
        #eventPriority = {"t0": PetriNets.Petri.Transition(1), "t1": PetriNets.Petri.Transition(1)}
        eventPriority = {"initial":1,"t0": 1, "t2": 1}
        transitionMatrix = [[-1, 1, 1, 0],
                            [0,0,-1,1],
                            [0,[-1,1],0,0],
                            [0,-1,0,-1]]



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
        beta="beta("+str(self.beta)+")"
        gamma="gamma("+str(self.gamma)+")"
        S0,I0,R0=str(self.initialS),str(self.initialI),str(self.initialR)
        sir="sir("+S0+","+I0+","+R0+",0)"
        sirKb = [beta, gamma, sir,
                 "simulatedays(SNext,INext,RNext,Dt):-sir(SPrev, IPrev, RPrev, DayPrev), Day is Dt+DayPrev, beta(Beta),gamma(Gamma),SNext is SPrev-Beta*SPrev*IPrev*Dt, INext is IPrev+(Beta*SPrev*IPrev-Gamma*IPrev)*Dt, RNext is RPrev+Gamma*IPrev*Dt, asserta(sir(SNext,INext,RNext,Day)),!"]
        self.SetKb(sirKb)
        beta="beta("+str(self.beta)+")"
        gamma="gamma("+str(self.gamma)+")"
        S0,I0,R0=str(self.initialS),str(self.initialI),str(self.initialR)
        sir="sir("+S0+","+I0+","+R0+",0)"

        self.petri.SetTransitionFacts({"initial": [beta,gamma,sir], "t0": "null", "t1":"null", "t2":"null"})
        self.petri.transitionPredicates={"initial":"null","t0":"null","t1":"simulatedays(SNext,INext,RNext,1)", "t2":"null"}
        self.petri.SetEventPriority({"initial":1,"t0":1,"t1":1, "t2":1})
    def LastState(self):
        res=self.Query("simulatedays(SNext,INext,RNext,1)")
        print("The Last Satete : ",res,"*")