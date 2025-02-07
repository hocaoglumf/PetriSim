import math
import random
def poisson_random_variable(lambda_param):
    L = math.exp(-lambda_param)
    k = 0
    p = 1
    while p > L:
        k += 1
        u = random.uniform(0, 1)
        p *= u
    return k - 1

# Örnek kullanım
lambda_param = 5
poissonRandomList=[]
for i in range(10):
    poissonRandomList.append(poisson_random_variable(lambda_param))
print(poissonRandomList)
