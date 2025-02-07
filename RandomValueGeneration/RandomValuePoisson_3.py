import math
import random
def poisson_random_variable_exponential(lambda_param):
    n = 0
    t = 0
    while True:
        u = random.uniform(0, 1)
        t += -math.log(u) / lambda_param
        if t > 1:  # 1 zaman birimi için
            break
        n += 1
    return n

# Örnek kullanım
lambda_param = 5
poissonRandomList=[]
for i in range(10):
    poissonRandomList.append(poisson_random_variable_exponential(lambda_param))
print(poissonRandomList)
