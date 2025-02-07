import PetriNets.SimNetScenario
import JobShopSim.AssemblyLine

#scenario1= PetriNets.SimNetScenario.SimNetScenario()


pg=JobShopSim.AssemblyLine.AssemblyLine()
pg.Initialize()
pg.SetName("Montaj Hattı")
transitionDurationCalculation = {"t0": -1, "t1": -1, "t2": "RandomValueGeneration.RandomValueCalculation.Normal(10.6,3)", "t3": -1,
                                 "t4": "RandomValueGeneration.RandomValueCalculation.Normal(11.6,4)", "t5": -1,
                                 "t6": "RandomValueGeneration.RandomValueCalculation.Normal(10.9,4)", "t7": -1,
                                 "t8": "RandomValueGeneration.RandomValueCalculation.Normal(17.5,6)", "t9": -1,
                                 "t10": "RandomValueGeneration.RandomValueCalculation.Normal(10.5,2)", "t11": -1, "t12": "RandomValueGeneration.RandomValueCalculation.Constant(105.91)",
                                 "t13": -1, "t14": -1, "t15": -1, "t16": -1, "t17": -1,
                                 "t18": "RandomValueGeneration.RandomValueCalculation.Normal(44.2,7)", "t19": -1,
                                 "t20": "RandomValueGeneration.RandomValueCalculation.Normal(34.8,5)", "t21": -1, "t22": "RandomValueGeneration.RandomValueCalculation.Constant(105.91)",
                                 "t23": -1, "t24": -1, "t25": -1, "t26": -1, "t27": -1,
                                 "t28": "RandomValueGeneration.RandomValueCalculation.Normal(10,4)", "t29": -1,
                                 "t30": "RandomValueGeneration.RandomValueCalculation.Normal(20,6)", "t31": -1,
                                 "t32": "RandomValueGeneration.RandomValueCalculation.Normal(43.8,9)", "t33": -1, "t34": "RandomValueGeneration.RandomValueCalculation.Constant(105.91)",
                                 "t35": -1, "t36": -1, "t37": -1, "t38": -1, "t39": -1,
                                 "t40": "RandomValueGeneration.RandomValueCalculation.Normal(5,2)", "t41": -1,
                                 "t42": "RandomValueGeneration.RandomValueCalculation.Normal(26.2,4)", "t43": -1,
                                 "t44": "RandomValueGeneration.RandomValueCalculation.Normal(29.2,4)", "t45": -1,
                                 "t46": "RandomValueGeneration.RandomValueCalculation.Normal(20,3)", "t47": -1, "t48": "RandomValueGeneration.RandomValueCalculation.Constant(105.91)",
                                 "t49": -1, "t50": -1, "t51": -1}

pg.SetTransitionDurationCalculation(transitionDurationCalculation)

pc= PetriNets.PetriCoordinator.PetriCoordinator()

pg.SetChat(True)

pc.Join(pg)
pc.SetChat(True)
pc.SetExecutionDuration(5000)

#scenario1.Join(pc)
#scenario1.Run(3)

pc.Run()

