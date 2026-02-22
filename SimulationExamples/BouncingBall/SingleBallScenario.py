
import SimulationExamples.BouncingBall
import BouncingBall
import PetriNets.PetriCoordinator as Pc

ball=BouncingBall.Ball()
ball.Initialize()
ball.SetName("Top1")
ball.SetTransitionDurationCalculation({"Fall":0.1, "Bounce":0.01, "Stop":-1})
ball.SetTransitionStates({"Fall":0,"Bounce":0, "Stop":0})


pc= Pc.PetriCoordinator()
ball.SetChat(True)
pc.Join(ball)
pc.SetExecutionDuration(500)
pc.SetChat(True)
pc.Run()
