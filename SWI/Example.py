from pyswip import Prolog
Prolog.assertz("father(michael,john)")
print(list(Prolog.query("father(X,Y)")))