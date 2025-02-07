import Pytholog.PetriProlog as pprolog


petriExp=pprolog.PetriProlog(pprolog.pl,"friends")

petriExp.setKnowledgebase(["add(X):-asserta(smokes(X))","has_lot_work(daniel, 8)",
    "has_lot_work(david, 3)",
    "stress(X, P) :- has_lot_work(X, P2), P is P2 / 100",
    "to_smoke(X, Prob) :- stress(X, P1), friends(Y, X), influences(Y, X, P2), smokes(Y), Prob is P1 + P2",
    "to_have_asthma(X, 0.3) :- smokes(X)",
    "to_have_asthma(X, Prob) :- to_smoke(X, P2), Prob is P2 * 0.25",
    "friends(X, Y) :- friend(X, Y)",
    "friends(X, Y) :- friend(Y, X)",
    "influences(X, Y, 0.4) :- friends(X, Y)",
    "friend(peter, david)",
    "friend(peter, rebecca)",
    "friend(daniel, rebecca)",
    "smokes(peter)",
    "smokes(rebecca)"])
#petriExp.query("add(ali)")
petriExp.setKnowledgebase(["smokes(ali)","smokes(veli)"])
petriExp.setKnowledgebase(["smokes(kemal)","smokes(riza)"])
S0=petriExp.query("to_smoke(Who, P)")
SS=petriExp.query("smokes(X)")
print(SS)






