from PetriNets import Petri, PetriCoordinator
''' Çift Kasa Servis '''

transitionMatrix0=[
[1, 0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	],
[0,	0,	0,	0,	0,	0,	0	]]

transitionMatrix1=[
[-1, 1,	0,	0,	0,	0,	0	],
[0,	-1,	-1,	1,	0,	0,	0	],
[0,	-1,	0,	0,	0,	-1,	1	],
[0,	0,	1,	-1,	1,	0,	0	],
[0,	0,	0,	0,	1,	1,	-1	]]

transitionDurationCalculation ={"e0":3, "e1":-1,"e2":-1, "e3":5,"e4":6}
#state=[1,0,1,0,0,1,0]
state={"P0":1,"P1":0,"P2":1,"P3":0, "P4":0, "P5":1, "P6":0}
eventPriority={"e0":1, "e1":1, "e2":2,"e3":1, "e4":1}
#eventPriority={"e0":Petri.Event(1), "e1":Petri.Event(1), "e2":Petri.Event(2),"e3":Petri.Event(1), "e4":Petri.Event(1)}


pn= Petri.PetriNet()
pn.SetTransitionDurationCalculation(transitionDurationCalculation)
pn.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pn.SetState(state)
#pn.SetSimulationDuration(15000)
pn.SetEventPriority(eventPriority)
pn.SetSimulationName("Çift Kasa ")
#pn.Simulate()
'''nÜretim Hattı Sınırlı '''

transitionMatrix0=[]
transitionMatrix1=[
[-1,-1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	-2,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	-1,	1]]

transitionDurationCalculation={"T1.1":-1,
"T1.2":3,
"T2.0":-1,
"T2.1":-1,
"T2.2":4,
"T3.0":-1,
"T3.1":-1,
"T3.2":2,
"T4.1":-1,
"T4.2":5,
"T5.0":-1,
"T5.1":-1,
"T5.2":6,
"TC.0":-1,
"TC.1":5}


eventPriority={"T1.1":1,
"T1.2":1,
"T2.0":1,
"T2.1":1,
"T2.2":1,
"T3.0":1,
"T3.1":1,
"T3.2":1,
"T4.1":1,
"T4.2":1,
"T5.0":1,
"T5.1":1,
"T5.2":1,
"TC.0":1,
"TC.1":1}

#state=[150,	1,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	26,	1,	0,	0,	0,	1,	0,	0,	1,	0,	0]
state={"P0":150,	"P1":1,	"P2":0,	"P3":0,	"P4":0,	"P5":1,	"P6":0,	"P7":0,	"P8":0,	"P9":1,	"P10":0,"P11":0,"P12":26,"P13":1,"P14":0,"P15":0,
       "P16":0,	"P17":1,"P18":0,	"P19":0,"P20":1,	"P21":0,	"P22":0}

pn0= Petri.PetriNet()
pn0.SetTransitionDurationCalculation(transitionDurationCalculation)
pn0.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pn0.SetState(state)
pn0.SetEventPriority(eventPriority)
pn0.SetSimulationName("Sınırlı Girdi Üretim Hattı")
#pn.Simulate()

'''nÜretim Hattı Sınırlı '''

transitionMatrix0=[]
transitionMatrix1=[
[-1,-1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1,	1,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1, -1,	1,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	-2,	0,	0,	0,	0,	0,	0,	0, -1, -1,	1,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	-1,	1]]

transitionDurationCalculation={"T1.1":-1,
"T1.2":3,
"T2.0":-1,
"T2.1":-1,
"T2.2":4,
"T3.0":-1,
"T3.1":-1,
"T3.2":2,
"T4.1":-1,
"T4.2":5,
"T5.0":-1,
"T5.1":-1,
"T5.2":6,
"TC.0":-1,
"TC.1":5}


eventPriority={"T1.1":1,
"T1.2":1,
"T2.0":1,
"T2.1":1,
"T2.2":1,
"T3.0":1,
"T3.1":1,
"T3.2":1,
"T4.1":1,
"T4.2":1,
"T5.0":1,
"T5.1":1,
"T5.2":1,
"TC.0":1,
"TC.1":1}

#state=[350,	1,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	258,	1,	0,	0,	0,	1,	0,	0,	1,	0,	0]
state={"P0":350,	"P1":1,	"P2":0,	"P3":0,	"P4":0,	"P5":1,	"P6":0,	"P7":0,	"P8":0,	"P9":1,	"P10":0,"P11":0,"P12":268,"P13":1,"P14":0,"P15":0,
       "P16":0,	"P17":1,"P18":0,	"P19":0,"P20":1,	"P21":0,	"P22":0}

pn1= Petri.PetriNet()
pn1.SetTransitionDurationCalculation(transitionDurationCalculation)
pn1.SetTransitionMatrix(transitionMatrix0,transitionMatrix1)
pn1.SetState(state)
pn1.SetEventPriority(eventPriority)
pn1.SetSimulationName("Sınırlı Girdi Üretim Hattı-2")
#pn.Simulate()


#
#
#

pc= PetriCoordinator.PetriCoordinator()

pc.Join(pn)
pc.Join(pn0)
pc.Join(pn1)
pc.Run()


