# %%
import numpy as np

# %%
#Genere una matriz Q de 5x5 con elementos aleatorios reales en [1,10)
Q = np.random.random((5,5))*(9.999-1)+1
# %%
# Imprima el porcentaje de elementos de la matriz Q que están por encima del promedio.
print( np.array(Q > Q.mean()).sum() / Q.size )
# %%
#Genere una lista L con 15 listas de 100 números reales en [0,8)
L = [ np.random.random(100) * 7.999 for i in range(15) ]
# %%
# Genere una lista M con los promedios de cada una de las 15 listas de L, luego imprima el promedio de los promedios.
M = [ L[i].mean() for i in range(15) ]
print(np.array(M).mean())
# %%
# Emule el experimento de obtener la suma de dos dados y genere una lista aleatoria D con los resultados de 1000 lanzamientos
D = np.random.randint(1, 7, 1000) + np.random.randint(1, 7, 1000)
# %%
# Suponga que tiene una caja con dos canicas rojas, tres azules y 5 blancas.
# Quiere emular el proceso de sacar 3 canicas de la caja de forma que no se regresa la canica que ya se sacó (o sea sin remplazo)
# Cree una lista C con los resultados de 10 experimentos (es decir, una lista de 10 listas con 3 elementos).
# Puede utilizar números en vez de colores si lo considera necesario
caja_con_canicas = ['roja', 'roja', 'azul', 'azul', 'azul', 'blanca', 'blanca', 'blanca', 'blanca', 'blanca']
C = [ np.random.choice(caja_con_canicas, size = 3, replace = False) for i in range(10) ]

