import matplotlib.pyplot as plt
import PetriNets.SimulationEntity
import PetriNets.Petri
import random
import math
class Ball2(PetriNets.SimulationEntity.SimulationEntity):
    def __init__(self):
        super().__init__()
        self.factoryRef = None
        self.h=random.randint(1,10)
        self.v=random.randint(0,10)
        self.g=10
        self.t=0
        self.freefall=True
        self.t_last = - math.sqrt(2*self.h/self.g)
        self.hmax =self.h
        self.vmax =math.sqrt(2 * self.hmax * self.g)
        self.rho = 0.75  # Geri sekme katsayısı (coefficient of restitution)
        #self.dt=0.01
        self.T=[]
        self.H=[]
        self.x=[]
        self.y=[]

    def Initialize(self):
        transitionGuards = {"Fall": "isFreeFall", "Bounce": "isBouncing","Stop":"Stop"}
        timeGrantFunctions={"Fall": "null", "Bounce": "null", "Stop": "null" }
        exitFunctions={"Fall": "FreeFall", "Bounce": "Bouncing", "Stop":"null"}

        state0 = {"Fall": 1, "Stop": 0}
        eventPriority = {"Fall": 1, "Bounce": 1, "Stop":1}
        transitionMatrix = [[[-1,1],0],
                            [[-1,1],0],
                            [-1,1]]


        petri= PetriNets.Petri.PetriNet()
        self.SetPetri(petri)
        self.petri.SetGuards(transitionGuards)
        self.petri.SetTimeGrantFunctions(timeGrantFunctions)
        self.petri.SetExitFunctions(exitFunctions)
        self.petri.SetTransitionMatrix(transitionMatrix)
        self.petri.SetState(state0)
        self.petri.SetEventPriority(eventPriority)
        self.petri.SetOwner(self)
        self.petri.transitionPredicates ={"Fall": "null", "Bounce": "null", "Stop":"null"}
        self.petri.SetEventPriority({"Fall":1,"Bounce":1,"Stop":2})
        self.factoryRef = self#globals()['Ball']()

    def FreeFall(self,dt):
        hnew = self.h + self.v*dt - 0.5*self.g*dt**2
        if(hnew<0):
          self.t = self.t_last + 2*math.sqrt(2*self.hmax/self.g)
          self.freefall = False
          #self.t_last = self.t + self.tau
          self.h=0
        else:
          self.t = self.t + dt
          self.v = self.v - self.g*dt
          self.h = hnew
        print("  h: ", round(self.h,2), "  v: ", round(self.v,3))
        self.y.append(self.h)
        self.x.append(self.GetTime())
        return self.h

    def Bouncing(self, tau):
        self.t = self.t + tau
        self.vmax = self.vmax * self.rho
        self.v = self.vmax
        self.freefall = True
        self.h = 0

        return self.h

    def isFreeFall(self):
        return self.freefall

    def isBouncing(self):
        return not(self.freefall)

    def Process(self):
        h=0
        if (self.freefall):
            h=self.FreeFall()
        else:
            h=self.Bouncing()

        self.hmax = 0.5 * self.vmax ** 2/ self.g
        self.H.append(h)
        self.T.append(self.t)
        return self.hmax,h

    def Stop(self):
        durmaSarti=self.h <=0.001 and abs(self.v)<0.0001
        if durmaSarti:
            plt.plot(self.x,self.y)
            plt.show()
        return durmaSarti

