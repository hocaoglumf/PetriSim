
import SimulationExamples.BouncingBall
import BouncingBall2
import PetriNets.PetriCoordinator as Pc

ball=BouncingBall2.Ball2()
ball.Initialize()
ball.SetName("Top1")
ball.SetTransitionDurationCalculation({"Fall":0.1, "Bounce":0.01, "Stop":-1})
ball.SetTransitionStates({"Fall":0,"Bounce":0, "Stop":0})

ball0=BouncingBall2.Ball2()
ball0.Initialize()
ball0.SetName("Top2")
ball0.SetTransitionDurationCalculation({"Fall":0.1, "Bounce":0.01, "Stop":-1})
ball0.SetTransitionStates({"Fall":0,"Bounce":0, "Stop":0})


ball1=BouncingBall2.Ball2()
ball1.Initialize()
ball1.SetName("Top1")
ball1.SetTransitionDurationCalculation({"Fall":0.1, "Bounce":0.01, "Stop":-1})
ball1.SetTransitionStates({"Fall":0,"Bounce":0, "Stop":0})


pc= Pc.PetriCoordinator()
ball.SetChat(True)
pc.Join(ball)
pc.Join(ball0)
pc.Join(ball1)
pc.SetExecutionDuration(500)
pc.SetChat(True)
pc.Run()
