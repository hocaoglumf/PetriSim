import math
import random
def Geometric(prob):
    r=random.random()
    rval0 = math.log(1 - r) / math.log(1 - prob)
    rval=math.ceil(rval0)
    return rval, rval0

for i in range(100):

    print(Geometric(random.random()))