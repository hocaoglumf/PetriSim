import SimulationExamples.SaltBalance.Tank as ss
import SimulationExamples.SaltBalance.Valve as vl
import PetriNets.PetriCoordinator as Pc


tank=ss.Tank()
tank.Initialize()
tank.SetName("Tank")
tank.SetTransitionDurationCalculation({"t0": -1, "T0": 2000, "t1":1})
tank.SetTransitionStates({"t0":0,"T0":1,"t1":0}) #There is transition that is external transition allowed

valve=vl.Valve()
valve.Initialize()
valve.SetName("Valve")
tank.SetTransitionDurationCalculation({"turnOn": -1, "turnOff": 2000, "t0":1})
tank.SetTransitionStates({"turnOn":0,"turnOff":0,"t0":0}) #There is no transition that is external transition allowed

tank.AttachConnectedEntity(valve)

pc=Pc.PetriCoordinator()
tank.SetChat(True)
pc.Join(tank)
pc.SetExecutionDuration(20000)
pc.SetChat(True)
pc.Run()
