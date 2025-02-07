import PetriNets.PetriCoordinator



class SimNetScenario:
    def __init__(self):
        self.__scenarioCoordinators=[]
        self.__speedList=[]
    def Join(self,scenario):
        self.__scenarioCoordinators.append(scenario)

    def Run(self, replication):
        for i in self.__scenarioCoordinators:
            s= i.Run()
            self.__speedList.append(s)
            i.Reset()


