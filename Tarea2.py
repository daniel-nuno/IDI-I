# %%
import numpy as np
import pandas as pd

# %%
# Genere una lista L con los primeros 50 números naturales impares
L = list(range(1,101, 2))

# %%
# Convierta la lista L en un arreglo A
A = np.array(L)
# %%
# Imprima el 7mo número de A, los elementos en las posiciones 3 a 9 y los últimos 3 en orden descendente.
print(A[6], A[3:9], A[:-4:-1], sep = '\n')
# %%
# Genere un arreglo B con enteros iniciando en 20 descendiendo en 3 hasta el 5
B = np.array(list(range(20, 4, -3)))
# %%
# Invierta el arreglo B y guárdelo en C (use Slicing)
C = B[::-1]
# %%
# Genere un arreglo D con 100 puntos igualmente espaciados desde el 2 hasta el 30
D = np.linspace(2,30,100)
# %%
# Imprima el tamaño de paso usado para generar D
print(D[1] - D[0])
# %%
# Genere un arreglo E de 100 puntos igualmente espaciados de 5 a 100 guardados como enteros.
E = np.linspace(5,100,100).astype(int)
# %%
# Genere un arreglo I con los elementos de A que son múltiplos de 3
I = A[A % 3 == 0]
# %%
# Genere una matriz F de 10x10 a partir de los elementos de D tomados por filas.
F = np.reshape(D, (10,10))
# %%
# Genere una matriz G de 10x10 a partir de los elementos de E tomados por columnas.
G = np.reshape(E, (10,10), 'F')
# %%
# Genere la submatriz M de G con los elementos de sus filas 1 y 2 y columnas de la 3 a la 6.
M = G[:2, 3:7]
# %%
# Obtenga la matriz N a partir de los elementos de G elevados al cuadrado menos 3
N = G**2 - 3
# %%
# Imprima SI en caso de que la matriz N contenga algún múltiplo de 17 y NO en caso contrario.
print( 'SI' if len(N[N % 17 == 0]) != 0 else 'NO')

# %%
# Imprima la tercer fila de F y la cuarta columna de G
print(F[2], G[:,3], sep = '\n')
# %%
# Defina la matriz H como la suma de F y G
H = F + G
# %%
# Obtenga un arreglo J con los elementos de H que están en el intervalo (20,30)
J = H[np.logical_and(H>=20, H<=30)]
# %%
# Cambie los elementos de H menores de 30 por cero, guarde la matriz resultante en K.
K = H
K[K < 30] = 0
# K = np.where(H < 30, 0, H)
# %%
# Imprima la cantidad de columnas de K cuya suma es más de 500.
print( sum( list( K.sum( axis = 0 ) > 500 ) ) )
# %%
# Genere un arreglo Z con los promedios de cada columna de K
Z = K.mean( axis = 0 )
