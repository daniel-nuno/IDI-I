# %%
import numpy as np

A = np.array([[3,5],[7,11]])
# %%
A = np.array([[3,5],[7,11]])
B = np.array([[-2,4],[9,10]])
C = 3*A + B - np.identity(2)
D = np.append(A,B, axis = 1)
# %%
suma_D = D.sum()
numeros_pares = np.array(D % 2 == 0).sum()
# %%
F = np.reshape(np.array(range(1,101)), (10,10), 'F')
# %%
sum_10_20 = F[np.logical_and(F>=10, F<=20)].sum()
