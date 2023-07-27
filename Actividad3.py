# %%
import numpy as np

# %%
#seed
#np.random.seed(1)
#scalar 0-1
#random_x = np.random.random()
#random int
#random_x_int = np.random.randint()
#matrix o vector 0-1
#random_matrix = np.random.random((4,3))
#whatever list or array
#L = ['q', 'w', 'r', 'e', 't']
#choice de una lista
#choice_list = np.random.choice(L,10)

# %%
## actividad 3
# Inicialice la semilla de aleatoriedad con un valor fijo arbitrario
np.random.seed(1)

# %%
# Genere una lista G con los elementos {3,6,9,...,39}
G = list(range(3, 40, 3))
# %%
# Imprima una permutación aleatoria de los elementos de G.
#print(np.random.shuffle(G))
print(np.random.choice(G, size = 13, replace = False))

# %%
# Obtenga una lista H con 4 elementos de G seleccionados de forma aleatoria (sin reemplazo).
H = np.random.choice(G, size = 4, replace = False)
# %%
# Genere un arreglo L de 100 números aleatorios enteros en [5,100]
L = np.random.randint(5, 101, 100)
# %%
# Imprima la cantidad de números pares en L.
print(L[L % 2 == 0])
# %%
# Genere una lista M de 100 números aleatorios reales en [3,10)
M = np.random.random(100)*(10-3)+3
# %%
# Imprima la suma de los elementos de M
print(M.sum())
# %%
# Genere una lista R con 20 listas de 50 números reales en [0,10)
R = np.random.random((50,20))*10
# %%
