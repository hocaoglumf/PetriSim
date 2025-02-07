import SimulationExamples.SirandSeiard.Sir as ss
import PetriNets.PetriCoordinator as Pc


sir=ss.Sir()
sir.Initialize()
sir.SetName("SIR")
sir.SetTransitionDurationCalculation({"initial": -1, "t0": 2000, "t1":1, "t2":-1})
sir.SetTransitionStates({"t0":0,"t1":0,"t2":0,"t3":0,"t4":0,"t5":0}) #There is no transition that is external transition allowed


pc=Pc.PetriCoordinator()
sir.SetChat(True)
pc.Join(sir)
pc.SetExecutionDuration(20000)
pc.SetChat(True)
pc.Run()
