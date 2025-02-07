import pytholog as pl
new_kb = pl.KnowledgeBase("flavor")
new_kb(["likes(noor, sausage)",
        "likes(melissa, pasta)",
        "likes(dmitry, cookie)",
        "likes(nikita, sausage)",
        "likes(assel, limonade)",
        "food_type(gouda, cheese)",
        "food_type(ritz, cracker)",
        "food_type(steak, meat)",
        "food_type(sausage, meat)",
        "food_type(limonade, juice)",
        "food_type(cookie, dessert)",
        "flavor(sweet, dessert)",
        "flavor(savory, meat)",
        "flavor(savory, cheese)",
        "flavor(sweet, juice)",
        "food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z)",
        "dish_to_like(X, Y) :- likes(X, L), food_type(L, T), flavor(F, T), food_flavor(Y, F), neq(L, Y)"])

print(new_kb.query(pl.Expr("likes(noor, sausage)")))

from time import time
start = time()
print(new_kb.query(pl.Expr("food_flavor(What, sweet)")))
print(time() - start)

# query 2
start = time()
print(new_kb.query(pl.Expr("food_flavor(Food, sweet)")))
print(time() - start)

start = time()
print(new_kb.query(pl.Expr("dish_to_like(noor, What)")))
print(time() - start)


## new knowledge base object
city_color = pl.KnowledgeBase("city_color")
city_color([
    "different(red, green)",
    "different(red, blue)",
    "different(green, red)",
    "different(green, blue)",
    "different(blue, red)",
    "different(blue, green)",
    "coloring(A, M, G, T, F) :- different(M, T),different(M, A),different(A, T),different(A, M),different(A, G),different(A, F),different(G, F),different(G, T)"
])


## we will use [0] to return only one answer
## as prolog will give all possible combinations and answers
print(city_color.query(pl.Expr("coloring(Alabama, Mississippi, Georgia, Tennessee, Florida)"), cut = True))

# {'Alabama': 'blue',
#  'Mississippi': 'red',
#  'Georgia': 'red',
#  'Tennessee': 'green',
#  'Florida': 'green'}

sir=pl.KnowledgeBase("SIR")
sir(["beta(0.3)",
     "gamma(0.1)",
     "initial_susceptible(0.9)",
     "initial_infected(0.1)",
     "initial_recovered(0.0)",
     "sir(0,0.9,0.1,0.0,1)",
     "simulatedays(D,SNext,INext,RNext):-sir(DayPrev, SPrev, IPrev, RPrev, Dt), D is Dt+DayPrev, beta(Beta),gamma(Gamma),SNext is SPrev-Beta*SPrev*IPrev*Dt, INext is IPrev+(Beta*SPrev*IPrev-Gamma*IPrev)*Dt, RNext is RPrev+Gamma*IPrev*Dt"])

x=sir.query(pl.Expr("beta(X)"))
print("beta",x)
A=sir.query(pl.Expr("sir(A,S,I,R,Dt)"), cut=True)
print(A)
B=sir.query(pl.Expr("simulatedays(A,S,I,R)"))
print(B)

