# %%
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
# %%
# 1 a
dado = [1,2,2,3,4,6,10,12]
L = (np.random.choice(dado, size = 1000)
  + np.random.choice(dado, size = 1000))
Lcounter = Counter(L.tolist())
print(Lcounter.most_common(1),Lcounter.most_common()[-1], sep = '\n')

# %%
# 1 b
print( max(L.tolist(), key = L.tolist().count),
        min(L.tolist(), key = L.tolist().count), sep = '\n')
# %%
# 2 a
baraja = list(range(1,11)) * 4
runs = 50000
cartas = 5
mano = np.array( [ np.random.choice(baraja, size = cartas, replace = False).sum() for i in range(runs) ] )
print(sum(mano >  30) / runs * 100)
# %%
#2 b
mano = (np.random.choice(range(1,11), size = runs)
  + np.random.choice(range(1,11), size = runs)
  + np.random.choice(range(1,11), size = runs)
  + np.random.choice(range(1,11), size = runs)
  + np.random.choice(range(1,11), size = runs))

print(sum(mano >  30) / runs * 100)
# %%
# 3
runs = 500
M = np.random.binomial(12, 0.25, runs) * 100 / 12
# %%
# 4
N = [ np.random.normal(10, size = 60).mean() for i in range(30) ]
std_30_dias = np.std(N)
#plt.hist(N)
# %%
# 5
Q = np.random.normal(1.68, 0.14, 500)
estatura_promedio = Q.mean()
estatura_max = Q.max()
estatura_min = Q.min()
# %%
# 7
exp_list = np.random.exponential(scale = 10, size = 10000)
gamma_list = np.random.gamma(shape = 2, scale = 5, size = 10000)
plt.hist(exp_list, bins = 100, histtype='stepfilled',alpha = 0.2)
plt.hist(gamma_list, bins = 100, histtype='stepfilled', alpha = 0.2)
plt.show()

# %%
