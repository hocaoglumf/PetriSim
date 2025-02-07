'''
Doç. Dr. M. Fatih Hocaoğlu
İstanbul Medeniyet Üniversitesi
Endüstri Müh. Böl.
'''
import RandomValueGeneration.RandomValueCalculation
import SWI.PetriProlog as pprolog
import collections.abc

class Duration:
    def __init__(self, dur):
        self.duration=dur

    def isInf(self):
        return (self.duration ==-1)


class Transition:
    def __init__(self, priority, Rule="null"):
        self.ruleFunction=Rule
        self.priority = priority
        self.exitfunction = ""
        self.timeGrantFunction=""
        self.durationCalculation ="0"

    def SetExitFunction(self,exitF):
        self.exitfunction =exitF

    def SetExternalTransitionFunctions(self,externalF):
        self.externalTransitionFunctions=externalF

    def SetTimeGrantFunction(self, tgf):
        self.timeGrantFunction = tgf

class Token:
    def __init__(self):
        pass


class PetriNet:
    def __init__(self):
        self.__places={}
        self.eventFire={}
        self.eventPriority={}
        self.transitionDurationCalculation={}
        self.transitionDuration={}
        self.consumedTransitionDuration={}
        self.transitionMatrix0=[]
        self.transitionMatrix=[]
        self.conflicting=[]
        self.terminationTime=-1
        self.functions={}
        self.exitFunctions={}
        self.transitionstates={} # Burada external transition 0,1,2 tanımlanacak
        self.externalTransitionFunctions={}
        self.timeGrantFunctions={}
        self.guards={}
        self.timeRequested=0
        self.__simName="__none__"
        self.k=""
        self.ownerModel={}
        self.prolog= pprolog.PetriProlog()
        self.transitionFacts={}


    def AssertFacts(self, eventFireAux):
        for i in list(eventFireAux.keys()):
            if eventFireAux[i]==1:
                if i in list(self.transitionFacts.keys()):
                    for j in self.transitionFacts[i]:
                        self.prolog.SetKb(j)
        return


    def SetKb(self,kb):
        for i in kb:
            self.prolog.SetKb(i)

    def SetTransitionFacts(self,tf):
        self.transitionFacts=tf

    def CalculateTransitionMatrix(self):
        self.transitionMatrix=[]
        #entry -- Meth:Func:-1
        for i in self.transitionMatrix0:
            transitionLine=[]
            for j in i:
                if isinstance(j, (int, float)):
                    transitionLine.append(j)
                elif type(j)==list:
                    transitionLine.append(sum(j))
                else:
                    entry=j.split(":")
                    if len(entry)<3:
                        c=1
                    else:
                        c=int(entry[2])
                    if entry[0].lower()=="meth":
                        v = c*self.ownerModel.Factory(entry[1])
                    elif entry[0].lower()=="att":
                        v=c*getattr(self.ownerModel, entry[1])
                    elif entry[0]=="#":
                        v=c*self.GetTokenNumber(entry[1])
                    elif  isinstance(float(entry[0]), (int, float)):
                        v=0
                        for k in entry:
                            v +=float(k)
                    else:
                        v=c*3
                        pass
                    transitionLine.append(v)
            self.transitionMatrix.append(transitionLine)
        return

    def SetOwner(self, owner):
        self.ownerModel=owner

    def GetPlaces(self):
        return self.__places

    def GetState(self):
        return list(self.__places.values())

    def SetSimulationName(self, name):
        self.__simName = name

    def GetSimulationName(self):
        return self.__simName

    def SetGuards(self,g):
        self.guards=g

    def SetFunctions(self,f):
        self.functions=f

    def SetExitFunctions(self,f):
        self.exitFunctions=f

    def SetTimeGrantFunctions(self,f):
        self.timeGrantFunctions=f

    def SetSimulationDuration(self, duration):
        self.terminationTime=duration

    def SetEventPriority(self,eventPriority):
        self.eventPriority=eventPriority

    def SetEventFire(self,s):
        self.eventFire=s

    def SetState(self,s):
        self.__places=s

    def SetTransitionStates(self,ts):
        self.transitionstates=ts

    def SetTransitionDurationCalculation(self, transitionDurationCalculation):
        self.transitionDurationCalculation=transitionDurationCalculation
        self.SetProcessDurationFirstTime()

    def SetTransitionMatrix(self,s0,s1=[]):
        self.transitionMatrix0=s0
        #self.CalculateTransitionMatrix()
        '''
        self.transitionMatrix0=s0
        self.transitionMatrix1=s1
        if (len(self.transitionMatrix0)==0):
            self.transitionMatrix0= self.PrepareMatrix(self.transitionMatrix1)
        if (len(self.transitionMatrix1)==0):
            self.transitionMatrix1= self.PrepareMatrix(self.transitionMatrix0)
        self.transitionMatrix= self.MatrisTopla(self.transitionMatrix0,self.transitionMatrix1)
        '''
    def MatrisTopla(self,X,Y):
        M=[]
        for i in range(len(X)):
            s=[]
            for j in range(len(X[0])):
                s.append(X[i][j] +Y[i][j])
            M.append(s)
        return M



    def Transpose(seldf,A):
        AT=[]
        for i in range(0,len(A[0])):
            c=[]
            for j in range(0,len(A)):
                c.append(0)
            AT.append(c)
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                AT[j][i]=A[i][j]

        return AT

    def VektorXMatris(self,V,A):
        c=[]
        for i in A:
            c.append(self.VektorXVektor(V,i))
        return c

    def VektorXVektor(self,V0,V1):
        t=0
        for i in range(0,len(V0)):
            t+=V0[i]*V1[i]
        return t

    def MatrisXMatris(self,A,B):
        c=[]
        TB=self.Transpose(B)
        xx=self.VektorXMatris(A,TB)
        return xx

    def FindConflictingEvents(self):
        self.CalculateTransitionMatrix()
        for i in range(len(self.transitionMatrix[0])):
            s=0
            cnf=[]
            for j in range(len(self.transitionMatrix)):
               if (self.transitionMatrix[j][i]<0):
                    s +=1
                    cnf.append(list(self.eventPriority.keys())[j])
            if (s>1):
                self.conflicting.append(cnf)
        return
    def ProcessDuration(self,min):
        j=-1
        for i in self.transitionDuration.keys():
            j +=1
            if (self.transitionDuration[i]>=min and self.EventCondition(j)):
                self.transitionDuration[i]= self.transitionDuration[i]- min
                self.consumedTransitionDuration[i] +=min
                if self.transitionstates[i]>0:
                    if (self.transitionDuration[i]>0 and i in self.timeGrantFunctions):
                        self.ownerModel.Factory(self.timeGrantFunctions[i],min)
                if self.transitionstates[i]==2:
                    self.transitionDuration[i]=0
                    self.consumedTransitionDuration[i]=min

       # self.ownerModel.SetTime(self.ownerModel.GetTime()+min)
        self.CallExitFunctions(min)
        return

    def FindMinimumTime(self):
        mintime,mntk=self.EventFireforTime()
        return mintime,mntk

    def FindMinTime(self):
        min, ctrl=self.EventFireforTime()
        if (not(ctrl)):
            return -1, False

        x=self.eventFire
#        min=999999
#        k=""
#        for i in self.transitionDuration.keys():
#            if (min > self.transitionDuration[i] and
#                    self.transitionDuration[i]>0 and
#                    self.EventGuard(i)):
#                min = self.transitionDuration[i]
#                k=i
        if (self.timeRequested > 0 and self.timeRequested <= min):
            min = self.timeRequested
        else:
            self.timeRequested=min
#        self.k=k
        k=""
        for i in self.eventFire.keys():
            if self.eventFire[i]==1:
                k +=i
        return k,min

    def EventCondition(self,e):
        sayac=0
        t= True
        self.CalculateTransitionMatrix()
        for i in range(len(self.transitionMatrix[e])):
            r = False
            nmbr=0
            kp=isinstance(self.transitionMatrix[e][i], (int, float))
            d=type(self.transitionMatrix0[e][i])==list
            if kp:
                nmbr=self.transitionMatrix[e][i]
                r = nmbr < 0
            if d:
                liste=self.transitionMatrix0[e][i]
                nmbr=min(liste)
                r=nmbr<0
            if (r):
                howmanytokens=self.GetState()[i]
                t= t and howmanytokens>=abs(nmbr) and howmanytokens>0
                #t = t and self.GetState()[i] !=0
                #t = t and xx

        return t

    def EventGuard(self, event):
        b=True
        if (event in self.guards):
            guard=self.guards[event]
            b = self.ownerModel.Factory(guard)
        return b

    def EventFireforTime(self):
        j = -1
        mntk = False
        for i in self.transitionDuration.keys():
            j += 1
            pp = self.__places
            cntrl0 = (self.transitionDuration[i] >= 0.000000 )
            cntrl1 = self.EventCondition(j) and self.EventGuard(i)
            cntrl = cntrl0 and cntrl1
            self.eventFire[i] = int(cntrl)
            mntk = mntk or cntrl

        mintime=99999999999
        founds=[]
        for i in self.eventFire.keys():
            if (float(self.transitionDuration[i])<=mintime and self.eventFire[i]==1):
                mintime=self.transitionDuration[i]
                founds.append(i)

        for i in self.eventFire.keys():
            if i in founds:
                self.eventFire[i]=1
            else:
                self.eventFire[i]=0


        return mintime, mntk

    def ImmediateTransitions(self):
        sum=0
        j=-1
        for i in self.transitionDuration.keys():
            j +=1
            if self.transitionDuration[i]==-1 :
                toBe=self.CheckImmediateTransitionToBeFired(j,i)
                self.eventFire[i]=toBe
                sum +=toBe
            else:
                self.eventFire[i]=0
        return sum>0, self.eventFire

    def CheckImmediateTransitionToBeFired(self,j,transition):
        cntrl1 = self.EventCondition(j) and self.EventGuard(transition)
        return int(cntrl1)

    def EventFire(self):
        j=-1
        mntk=False
        for i in self.transitionDuration.keys():
            j +=1
            pp=self.__places
            cntrl0=(self.transitionDuration[i]==-1)
            cntrl1=self.EventCondition(j) and self.EventGuard(i)
            cntrl=cntrl0 and cntrl1
            ek=0
            if (i in self.eventFire.keys()):
                ek=self.eventFire[i]
            self.eventFire[i]=int(cntrl) +int(ek)
            mntk=mntk or cntrl

        # İste buraya matris çarpımı eklenecek
        # eğer evetFire[i]==1 ve süresi sıfır ise eventFire=1 kalacak değilse sıfır olacak ve matisle çarpılacak
        eventVector={}
        for i in list(self.eventFire.keys()):
            if self.transitionDuration[i]>0 and self.eventFire[i]==1:
                self.eventFire[i]=0


        self.EventFireProcess(self.eventFire, 0)

        return mntk

    def Sum(self,x,y):
        sum=[]
        for i in range(len(x)):
            sum.append(x[i]+y[i])
        return sum

    def SetProcessDurationFirstTime(self):
        karakter=type("k")
        j=-1
        for i in self.transitionDurationCalculation.keys():
            j +=1
            cntrl = self.EventCondition(j)
            self.consumedTransitionDuration[i]=0
            if (type(self.transitionDurationCalculation[i]) == karakter and cntrl):
                func = self.transitionDurationCalculation[i]
                self.transitionDuration[i] = round(eval(func),3)
            elif (type(self.transitionDurationCalculation[i]) == karakter and not(cntrl)):
                self.transitionDuration[i]=-1
            else:
                self.transitionDuration[i] = self.transitionDurationCalculation[i]
        return

    def SetProcessDurations(self):
        karakter=type("k")
        durationFound = -1
        j=-1
        for i in self.transitionDurationCalculation.keys():
            dr = self.transitionDuration[i]
            j +=1
            cntrl = self.EventCondition(j)
            self.eventFire[i]=0
            if (dr ==0):
                if (type(self.transitionDurationCalculation[i])==karakter and cntrl ):
                    func=self.transitionDurationCalculation[i]
                    durationFound = round(eval(func),3)
                    self.transitionDuration[i] = durationFound
                    self.consumedTransitionDuration[i] = 0
                    self.eventFire[i]=1
                elif (type(self.transitionDurationCalculation[i])==karakter and not(cntrl)):
                    self.transitionDuration[i] =-1
                    self.eventFire[i] = 0
                else:
                    self.transitionDuration[i] = self.transitionDurationCalculation[i]
                    self.eventFire[i] = int(cntrl)
        return durationFound

    def ResetEventFire(self, eventFireAux):
        for i in self.eventFire.keys():
            if (self.eventFire[i] == eventFireAux[i]):
                self.eventFire[i]=0

    def ThereEventToFire(self, eventFireAux):
        return sum(eventFireAux.values())>0

    def FireTheEvents(self, eventFireAux):
        for i in self.conflicting:
            for j in range(len(i)-1):
                for k in range(j+1,len(i)):
                    if (eventFireAux[i[j]] ==1 and  eventFireAux[i[k]]==1):
                        ii=0
                        b0= self.eventPriority[i[j]].priority < self.eventPriority[i[k]].priority
                        b1 = eval(self.eventPriority[i[j]].ruleFunction)
                        if (b0):
                            eventFireAux[i[k]]=0
                        else:
                            eventFireAux[i[j]] = 0
        return eventFireAux

    def CallFunctions(self, func, duration):
        eval(func(duration))
        return


    def Initialize(self):

        if (len(self.eventFire)==0):
            for i in self.transitionDurationCalculation.keys():
                self.eventFire[i]=0
        self.FindConflictingEvents()

    def EventFireControl(self):
        mntk = self.EventFire()
        eventFireAux = {}
        eventFireAux = self.eventFire
        return mntk, eventFireAux

    def CallExitFunctions(self, min):
        eventFireAux=self.eventFire
        for i in eventFireAux.keys():
            if (eventFireAux[i]==1 and self.transitionDuration[i]==0.00000):
                try:
                    self.ownerModel.Factory(self.exitFunctions[i],min)
                except ValueError:
                    print(self.ownerModel.GetName(), "  ",self.timeGrantFunctions[i])

    def FireEventVector(self):
        mtr=list(self.eventFire.values())
        res = self.MatrisXMatris(mtr, self.transitionMatrix)
        state = self.Sum(self.GetState(), res)
        self.UpdatePlaces(state)

    def NoEvent(self):
        return sum(self.eventFire.values())

    def ResetEventVector(self):
        for i in list(self.eventFire.keys()):
            self.eventFire[i]=0

    def EventFireProcess(self, eventFireAux,min ):
        self.CalculateTransitionMatrix()
        self.CallExitFunctions(min)
        while self.ThereEventToFire(eventFireAux):
            self.FireTheEvents(eventFireAux)
            mtr = []
            state=[]
            mtr.append(list(eventFireAux.values()))
            res = self.MatrisXMatris(mtr, self.transitionMatrix)
            state = self.Sum(self.GetState(), res)
            self.UpdatePlaces(state)
            # Burada factler atanıyor
            self.AssertFacts(eventFireAux)

            self.ResetEventFire(eventFireAux)

    def UpdatePlaces(self, state):
        keys = list(self.__places.keys())
        values = list(self.__places.values())
        for i in range(0,len(state)):
            self.__places[ keys[i] ]=state[i]


    def GetTokenNumber(self,place):
        return self.__places[place]

    def PutToken(self,place, n):
        self.__places[place]=self.__places[place] + n

    def EventandTime(self, min):
        return self.FireEvents(min)

    def CheckTimeGrantCondition(self):
        eventsToBeFired = self.EventFireControl()
        for i in eventsToBeFired.keys():
            bl = eventsToBeFired[i]==1 and self.transitionDurationCalculation[i]==-1
            if (bl):
                return False
        return True

    def TriggetTransitionsLog(self, events):
        log=""
        for i in list(events.keys()):
            if (events[i]==1):
                log +=i +"  "
        if (len(log)>0):
            log = "Tetiklenen olaylar : " +log + "Zaman   (" + str(round(self.ownerModel.GetTime(), 2)) + ")"

            print (log)

    def SelectHighestPriorityTransition(self):
        if sum(self.eventFire.values())<=1:
            return

        highest=-1
        for i in self.eventFire.keys():
            if i in self.eventPriority.keys():
                if (self.eventPriority[i]>highest and self.eventFire[i]==1):
                    highest=self.eventPriority[i]
        cnt=True
        for i in self.eventFire.keys():
            if (cnt and self.transitionDurationCalculation[i]==-1 and self.eventFire[i]==1 and self.eventPriority[i]==highest):
                self.eventFire[i]=1
                cnt=False
            else:
                self.eventFire[i]=0

    def FireEventsForTime(self,min):
        self.EventFireProcess(self.eventFire, min)

    def FireEvents(self,min):

        mntk, eventFireAux = self.EventFireControl()
        self.TriggetTransitionsLog(eventFireAux)

        self.SelectHighestPriorityTransition()

        self.EventFireProcess(eventFireAux, min)

        return mntk


