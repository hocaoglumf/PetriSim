'''
Doç. Dr. M. Fatih Hocaoğlu (Assoc. Prof.)
Istanbul Medeniyet University
'''
import threading
from datetime import datetime


from PetriNets import Petri
import time

class ConvertTime:
    def __init__(self):
        self.time = time.time()

    def Convert(self,sn):
        self.time +=sn
        self.time = self.time % (24 * 3600)
        hour = round(self.time // 3600)
        self.time %= 3600
        minutes = round(self.time // 60)
        self.time %= 60
        seconds = round(self.time)
        zmn=f"{hour:02d}:{minutes:02d}:{seconds:02d}"
        return zmn


class PetriCoordinator:
    def __init__(self):
        self.petrinets=[]
        self.clock=0
        self.terminationTime=-1
        self.transitions=[]
        self.timer = ConvertTime()
        self.current_timeStart=0
        self.chat=False

    def SetExecutionDuration(self,exdur):
        self.terminationTime=exdur

    def Join(self,p):
        self.petrinets.append(p)

    def AttachTransition(self,t):
        self.transitions.append(t)


    def Initialize(self):
        for i in self.petrinets:
            i.Initialize()

    def FindMinTime(self):
        gk=""
        simName=""
        min = 999999999999999
        for i in self.petrinets:
            name=i.GetSimulationName()
            try:
                k,minf=i.FindMinTime()
            except:
                print("There is something wrong!")
            if (minf <=0):
                minf =9999999999999
            if (min > minf):
                simName=name
                min =minf
            try:
                if (len(gk)==0):
                    gk=k
            except Exception as  e:
                print("gk=",k)

        return simName, gk, min

    def ProcessDuration(self, min):
        minr=0
        for i in self.petrinets:
            i.SetTime(min)
            i.ProcessDuration(min)
        return minr

    def ProcessDurationMultiThread(self, min):
        processList=[]
        for i in self.petrinets:
            t1 = threading.Thread(target=self.ProcessDuration, args=(min,))
            processList.append(t1)

        for i in processList:
            i.start()

        for i in processList:
            i.join()

        return min

    def Transitions(self):
        for i in self.petrinets:
            i.Transitions()

        for i in self.transitions:
            self.Transition(i[0], i[1],i[2],i[3],i[4],i[5])

    def Transition(self, pFrom, placeFrom, weightFrom,pTo, placeTo,weightTo):
        if (pFrom.GetTokenNumber(placeFrom)>=weightFrom):
            pFrom.PutToken(placeFrom,-1*weightFrom)
            pTo.PutToken(placeTo,weightTo)


    def EventFireforTime(self):
        for i in self.petrinets:
            i.EventFireforTime()

    def EventandTime(self, min):
        mntk =False
        for i in self.petrinets:
            mntk =  mntk or i.EventandTime(min)
            self.Transitions()
        return mntk

    def SetProcessDurations(self):
        for i in self.petrinets:
            i.SetProcessDurations()
            i.FireEventVector()

    def SimLog(self,step):
        if (self.chat):
            for i in self.petrinets:
                if (i.GetChat()):
                    if step<99999999:
                        print(i.GetSimulationName(), "  ", i.GetPlaces(), " Time: ",i.GetTime())
                    else:
                        print(i.GetSimulationName(), "  ", i.GetPlaces(), " Time: -")

    def LogSimTime(self):
        if (self.chat):
            log = "  Zaman " + str(self.timer.Convert(self.clock)) + "  (" + str(round(self.clock, 4)) + ")"
            print (log)

    def GoodbyNote(self):
        self.SetChat(True)
        self.LogSimTime()
        #self.SimLog(minTime)
        self.SetChat(False)
        now = datetime.now()
        current_timeFinish = now
        print("Current Time =", current_timeFinish)
        diff=(current_timeFinish - self.current_timeStart)
        try:
            print("Execution Speed :", round(self.clock/(diff.days*24*60*60 + diff.seconds),3),"X" )
        except ZeroDivisionError:
            print("Execution Speed : -")

    def SetChat(self, T):
        self.chat = T

    def SimLegend(self):
        now = datetime.now()
        self.current_timeStart = now
        print("Current Time ::", self.current_timeStart)
        print ("Simulation Entities ")
        print ("---------------------")
        for i in self.petrinets:
            print(i.GetSimulationName())
        print("Exection Duration ::", self.terminationTime)
        print("-------------------------")

    def Reset(self):
        for i in self.petrinets:
            i.Reset()

    def CalculateSpeed(self):
        now = datetime.now()
        current_timeFinish = now
        print("Current Time =", current_timeFinish)
        diff = (current_timeFinish - self.current_timeStart)
        speed=0

        try:
            speed =round(self.clock*10**6 / (diff.microseconds), 3)
        except ZeroDivisionError:
            print("Zero div. !")
        print("Speed : ", speed,"X", "  Execution Duration: ", diff.seconds, " sec.")
        return speed

    def CheckTimeGrantCondition(self):
        for i in self.petrinets:
            b = i.CheckTimeGrantCondition()
            if (not(b)):
                return False
        return True

    def ImmediateEventControl(self, step):
        r=True
        while (r):
            mntk = self.EventandTime(step)
            #self.SimLog()
#            if (mntk):
#                self.SetProcessDurations()
            r =mntk
        return

    def SetClock(self):
        for i in self.petrinets:
            i.SetTime(self.clock)

    def FireEventsForTime(self, min):
        for i in self.petrinets:
            i.FireEventsForTime(min)

    def ImmediateConflictControl(self,petri):
        max=0
        for event, fired in petri.petri.eventFire.items():
            pri=petri.petri.eventPriority[event]
            if fired>0 and pri>max:
                max =pri
        for i in list(petri.petri.eventFire.keys()):
            if petri.petri.eventPriority[i]<max:
                petri.petri.eventFire[i]=0

    def ImmediateTransitions(self):
        for i in self.petrinets:
            immediateCont=True
            while immediateCont:
                immediateCont, events = i.ImmediateTransitions()
                self.ImmediateConflictControl(i)
                if immediateCont:
                    if immediateCont:
                        i.FireEventVector()
                        # Firing burada ateşleme yapılacak
        return

    def FindMinimumTime(self):
        minT=99999999
        for i in self.petrinets:
            found, mtk=i.FindMinimumTime()
            if minT>found:
                minT=found
        return minT
    def NoEvent(self):
        noEvent=0
        for i in self.petrinets:
            noEvent += i.NoEvent()
        return noEvent==0

    def ResetEventVector(self):
        for i in self.petrinets:
            i.ResetEventVector()

    def Run(self):
        self.SimLegend()
        while True:
            self.ResetEventVector()
            self.ImmediateTransitions()
            self.Transitions()
            # Find Min time
            minTime=self.FindMinimumTime()
            # Time Grand
            self.ProcessDuration(minTime)
            self.clock +=minTime
            self.SetProcessDurations()
            self.Transitions()
            self.SimLog(minTime)
            if self.NoEvent():
                print("There is nothing to do. Goodbye cruel world...")
                return self.CalculateSpeed()

            if (self.terminationTime <=self.clock and self.terminationTime >0 ):
                self.GoodbyNote()
                print("The time is up...Goodbye cruel world...")
                return self.CalculateSpeed()

    def GetMinNumberofToken(self,type,place):
        mintoken=99999999
        for i in self.petrinets:
            if i.type==type:
                n = i.GetTokenNumber(place)
                if n<mintoken:
                    mintoken=n
        return mintoken

    def Run_ex(self):
        self.SimLegend()
        gk=""
        #self.Initialize()
        print("All entities are initialized.")
        print("Simulation Started...")
        self.Transitions()
        self.ImmediateEventControl(0)

        #self.SetProcessDurations()
        while True:
            simName, k,min=self.FindMinTime()
            min = self.ProcessDuration(min)
            self.clock +=float(min)
            self.SetClock()
            self.LogSimTime()
            self.SimLog()
      #      self.FireEventsForTime(min)
            self.EventandTime(min)
            self.ImmediateEventControl(min)
            self.SetProcessDurations()

            if (len(str(k))==0): # düzgün bir sonlanma şartı konulacak
                self.GoodbyNote()
                print("There is nothing to do, the simulation is over.")
                return self.CalculateSpeed()

            if (self.terminationTime <=self.clock and self.terminationTime >0 ):
                self.GoodbyNote()
                print("The time is up...Goodbye cruel world...")
                return self.CalculateSpeed()

