from pyswip import Prolog

sirKb=["beta(0.3)",
     "gamma(0.1)",
     "sir(0.9,0.1,0.0,0)",
     "simulatedays(SNext,INext,RNext,Dt):-sir(SPrev, IPrev, RPrev, DayPrev), Day is Dt+DayPrev, beta(Beta),gamma(Gamma),SNext is SPrev-Beta*SPrev*IPrev*Dt, INext is IPrev+(Beta*SPrev*IPrev-Gamma*IPrev)*Dt, RNext is RPrev+Gamma*IPrev*Dt, asserta(sir(SNext,INext,RNext,Day)),!"]

for i in sirKb:
    Prolog.assertz(i)
day=0
N=5
while True:
    q=Prolog.query("simulatedays(SNext,INext,RNext,1)")
    print(list(q))
    w0=list(Prolog.query("sir(S0,I0,R0,_)"))
    day +=1
    x0=round((float(w0[0]['S0'])-float(w0[1]['S0'])),N) ==0
    x1=round((float(w0[0]['R0']) - float(w0[1]['R0'])), N) == 0
    if  x0 and x1:
        print(w0[0]['S0'], " ", w0[1]['S0'])
        print(w0[0]['R0'], " ", w0[1]['R0'])

        print(day)
        break

