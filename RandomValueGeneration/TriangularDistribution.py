import random

def Triangular(a,b,c):
    Rn=random.random()
    CDF_TriMode=(b-a)/(c-a)
    if (Rn>0 and Rn<CDF_TriMode):
        y = a + (Rn*(c-a)*(b-a))**.5
    else:
        y = c- ((1-Rn)*(c-a)*(c-b))**.5
    return y
r=0
iter=0
while r<7.998:
    iter +=1
    r=Triangular(2,5,8)
print(r,"  ",iter)