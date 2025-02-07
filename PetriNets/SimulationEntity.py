import PetriNets
import inspect
import collections
class SimulationEntity:
    def __init__(self):
        self.type=""
        self.petri=None
        self.__chat=False
        self.factoryRef = None
        self.time=0
        self.coordinator=None

    def SetType(self,type):
        self.type=type

    def Initialize(self):
        self.factoryRef = globals()['SimulationEntity']()

    def SetChat(self,c):
        self.__chat=c

    def GetChat(self):
        return self.__chat

    def SetTime(self,time):
        self.time +=time

    def GetTime(self):
        return self.time

    def SetName(self, name):
        self.petri.SetSimulationName(name)

    def GetSimulationName(self):
        return self.petri.GetSimulationName()

    def GetTokenNumber(self, place):
        return self.petri.GetTokenNumber(place)

    def GetPlaces(self):
        return self.petri.GetPlaces()

    def PutToken(self,place, token):
        return self.petri.PutToken(place, token)

    def FindMinimumTime(self):
        return self.petri.FindMinimumTime()

    def FindMinTime(self):
        return self.petri.FindMinTime()

    def ProcessDuration(self,min):
        return self.petri.ProcessDuration(min)

    def FireEventsForTime(self,min):
        return self.petri.FireEventsForTime(min)

    def EventandTime(self, min):
        return self.petri.EventandTime(min)

    def EventFireforTime(self):
        return self.petri.EventFireforTime()


    def SetProcessDurations(self):
        self.petri.SetProcessDurations()

    def SetState(self,state):
        self.petri.SetState(state)

    def SetTransitionDurationCalculation(self, dc):
        self.petri.SetTransitionDurationCalculation(dc)

    def SetTransitionStates(self,ts):
        self.petri.SetTransitionStates(ts)

    def SetPetri(self,petri):
        self.petri=petri

    def SetTimeGrantFunctions(self,f ):
        self.petri.SetTimeGrantFunction(f)

    def SetExitFunctions(self,f):
        self.petri.SetExitFunction(f)

    def SetExternalTransitionFunctions(self,f):
        self.petri.SetExternalTransitionFunctions(f)

    def CheckTimeGrantCondition(self):
        return self.petri.CheckTimeGrantCondition()


    def null(self):
        return True

    def SetKb(self,kb):
        self.petri.SetKb(kb)

    def Factory(self,meth, *paramset):
        func = getattr(self.factoryRef, meth, *paramset)
        l = inspect.signature(func)
        if len(str(l))==2:
            return func()
        else:
            return func(*paramset)
    def SetTransitionStates(self,transitionStates):
        self.petri.SetTransitionStates(transitionStates)


    def ImmediateTransitions(self):
        return self.petri.ImmediateTransitions()

    def FireEventVector(self):
        self.petri.FireEventVector()

    def NoEvent(self):
        return self.petri.NoEvent()

    def ResetEventVector(self):
        self.petri.ResetEventVector()