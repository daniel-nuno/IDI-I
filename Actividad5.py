# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
N = 1000
a = 1
b = 4

x = [ np.mean( 1 / (np.random.uniform(a, b, N)**2 + 4) ) * (b - a) for i in range(100) ]
# %%
np.mean(x)
np.std(x)
# %%
valor_esperado = 1/4 * np.arctan(24/7)
error_absoluto = abs(np.mean(x) - valor_esperado)
error_relativo = (np.mean(x) -  valor_esperado) / valor_esperado * 100
# %%
