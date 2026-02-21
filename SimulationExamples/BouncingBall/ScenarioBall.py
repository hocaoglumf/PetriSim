
import SimulationExamples.BouncingBall
import BouncingBall
import PetriNets.PetriCoordinator as Pc

ball=BouncingBall.Ball()
ball.Initialize()
ball.SetName("Top1")
ball.SetTransitionDurationCalculation({"t0": -1, "t1": 0.01, "t2":-1, "t3":-1, "t4":0.001, "t5":-1})
ball.SetTransitionStates({"t0":0,"t1":0,"t2":0,"t3":0,"t4":0,"t5":0})

ball0=BouncingBall.Ball()
ball0.Initialize()
ball0.SetName("Top2")
ball0.SetTransitionDurationCalculation({"t0": -1, "t1": 0.01, "t2":-1, "t3":-1, "t4":0.001, "t5":-1})
ball0.SetTransitionStates({"t0":0,"t1":0,"t2":0,"t3":0,"t4":0,"t5":0})

ball1= BouncingBall.Ball()
ball1.Initialize()
ball1.SetName("Top3")
ball1.SetTransitionDurationCalculation({"t0": -1, "t1": 0.01, "t2":-1, "t3":-1, "t4":0.001, "t5":-1})
ball1.SetTransitionStates({"t0":0,"t1":0,"t2":0,"t3":0,"t4":0,"t5":0})

pc= Pc.PetriCoordinator()
ball.SetChat(True)
pc.Join(ball)
pc.Join(ball0)
pc.Join(ball1)
pc.SetExecutionDuration(500)
pc.SetChat(True)
pc.Run()
