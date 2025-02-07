from pyswip import Prolog

class PetriProlog:
    def __index__(self):
        self.kb=[]

    def SetKb(self,kb):
        Prolog.assertz(kb)

    def Query(self,q):
        return list(Prolog.query(q))

'''
sir=PetriProlog()
sirKb=["beta(0.3)",
     "gamma(0.1)",
     "sir(0.9,0.1,0.0,0)",
     "simulatedays(SNext,INext,RNext,Dt):-sir(SPrev, IPrev, RPrev, DayPrev), Day is Dt+DayPrev, beta(Beta),gamma(Gamma),SNext is SPrev-Beta*SPrev*IPrev*Dt, INext is IPrev+(Beta*SPrev*IPrev-Gamma*IPrev)*Dt, RNext is RPrev+Gamma*IPrev*Dt, asserta(sir(SNext,INext,RNext,Day)),!"]
sir.SetKb(sirKb)

Result=sir.Query("simulatedays(SNext,INext,RNext,1)")
print(Result)
Result=sir.Query("simulatedays(SNext,INext,RNext,1)")
print(Result)
'''