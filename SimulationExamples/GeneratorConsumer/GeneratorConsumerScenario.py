import SimulationExamples.GeneratorConsumer.Consumer as consumer
import SimulationExamples.GeneratorConsumer.Generator as generator

import PetriNets.PetriCoordinator as Pc

pc=Pc.PetriCoordinator()

gen=generator.Generator()
gen.Initialize()
gen.SetType("Generator")
gen.SetName("Generator")
gen.SetTransitionDurationCalculation({"t4": 2})
gen.SetTransitionStates({"t4":0}) #There is no transition that is external transition allowed

cons0=consumer.Consumer()
cons0.SetType("Consumer")
cons0.Initialize()
cons0.coordinator=pc
pc.Join(cons0)
cons0.SetName("Consumer0")

cons1=consumer.Consumer()
cons1.SetType("Consumer")
cons1.Initialize()
cons1.coordinator=pc
#pc.Join(cons1)
cons1.SetName("Consumer1")

cons0.SetTransitionDurationCalculation({"t0": 7, "t1": -1, "t2": 6, "t3": -1})
cons1.SetTransitionDurationCalculation({"t0": 7, "t1": -1, "t2": 6, "t3": -1})

gen.SetChat(True)
cons0.SetChat(True)
pc.Join(gen)

gen.AttachConnectedEntity(cons0)
gen.AttachConnectedEntity(cons1)

#gen.AttachPort("Consumer","P5",1,"inPort",1)
gen.AttachPort(cons0,"P5",1,"inPort",gen.MinimumOne(cons0))
gen.AttachPort(cons1,"P5",1,"inPort",gen.MinimumOne(cons1))


#pc.AttachTransition([gen,"P5", 1, cons0, "inPort",1])

pc.SetExecutionDuration(50)
pc.SetChat(True)

pc.Run()
