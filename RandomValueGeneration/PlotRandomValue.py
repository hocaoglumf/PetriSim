from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#sns.distplot(random.normal(size=1000), hist=False)

rn=[]
for i in range(100):
    rn.append(round(random.poisson(4),4))


plt.ylabel("Yoğunluk" )
plt.xlabel("Rassal Değer" )
print(rn)
#sns.distplot(rn, hist=False)
sns.histplot(
    rn, kde=True,
    stat="density", kde_kws=dict(cut=3),
    alpha=.4, edgecolor=(1, 1, 1, .4))
#sns.distplot(rn, hist=False)

plt.show()