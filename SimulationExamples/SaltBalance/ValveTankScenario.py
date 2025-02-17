import SimulationExamples.SaltBalance.Tank as ss
import SimulationExamples.SaltBalance.Valve as vl
import PetriNets.PetriCoordinator as Pc


tank=ss.Tank()
valve=vl.Valve()
tank.AttachConnectedEntity(valve)

tank.Initialize()
tank.SetName("Tank")

valve.Initialize()
valve.SetName("Valve")

valve.AttachPort(tank, "OutPort0",1,"InPort0",1)

pc=Pc.PetriCoordinator()
tank.SetChat(True)
pc.Join(tank)
pc.Join(valve)
pc.SetExecutionDuration(20000)
pc.SetChat(True)
pc.Run()
