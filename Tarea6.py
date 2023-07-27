# Realice código en Python para implementar el algoritmo Simulated Annealing
# para resolver un problema de TSP.
# Es decir, dadas N ubicaciones y su matriz de distancias, encontrar una ruta cíclica óptima (de menor distancia) entre ellas.
# Puede realizar pruebas con las siguientes matrices.

# %%
import pandas as pd
import numpy as np

# %%
# condiciones de función de energia:
#   1.- tiene que pasar por todas las ciudades
#   2.- tiene secuencia, de donde esta tiene que ir a otro lado, y a donde llego tiene que ir a otro
#   3.- no repetirse la ciudad
#   4.- de donde inicia tiene que terminar
# sumatoria de la dista
# configuración inicial:

def funcion_energia_tsp(df_distancias, list_ciudades):
    list_ciudades_tmp = list_ciudades[:]
    ciudad_inicial = np.random.choice(list_ciudades_tmp, size = 1)[0]
    ciudad_actual = ciudad_inicial
    ciudades_visitadas = [ciudad_inicial]
    list_ciudades_tmp.remove(ciudad_inicial)
    distancia = 0

    for _ in range(len(list_ciudades_tmp)):
        siguiente_ciudad = np.random.choice(list_ciudades_tmp, size = 1)[0]
        distancia = distancia + df_distancias.at[ciudad_actual, siguiente_ciudad]
        ciudad_actual = siguiente_ciudad
        ciudades_visitadas.append(siguiente_ciudad)
        list_ciudades_tmp.remove(siguiente_ciudad)
    
    distancia = distancia + df_distancias.at[ciudad_actual, ciudad_inicial]

    return ciudades_visitadas, distancia

def temperature_function(T0, t):
    return  T0 / np.log(1 + t)

# %%
####################### 8 ciudades
#######################
df_ciudades = pd.read_excel('C:/Users/nuno/Downloads/probarSimAnn.xlsx', sheet_name='8c', index_col=0)
lista_ciudades = list(df_ciudades.index.values)

initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
T0 = 2000
t = 0
epochs = 20

# %%
while temperature_function(T0, t) > 10:
    for _ in range(epochs):
        ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
        delta_x = prime_x - initial_x
        q = np.exp(-delta_x / temperature_function(T0, t))
        p = np.random.uniform()
        if p < q:
            initial_x = prime_x
            ciudades_visitadas = ciudades_prime_x
    t = t + 1

print('la mejor ruta es: ', ciudades_visitadas)
# %%
####################### 15 ciudades
#######################
df_ciudades = pd.read_excel('C:/Users/nuno/Downloads/probarSimAnn.xlsx', sheet_name='15c', index_col=0)
lista_ciudades = list(df_ciudades.index.values)

initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
T0 = 1000
t = 0
epochs = 1000

# %%
while temperature_function(T0, t) > 150:
    for _ in range(epochs):
        ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
        delta_x = prime_x - initial_x
        q = np.exp(-delta_x / temperature_function(T0, t))
        p = np.random.uniform()
        if p < q:
            initial_x = prime_x
            ciudades_visitadas = ciudades_prime_x
    t = t + 1

print('la mejor ruta es: ', ciudades_visitadas)
#la mejor ruta es:  ['Acatlán de Juárez', 'Acámbaro', 'Acuitlapilco', 'Acala', 'Acanceh', 'Acayucan', 'Acatzingo', 'Acapulco de Juárez', 'Acatlán de Osorio', 'Acajete', 'Actopan', 'Abasolo', 'Acatic', 'Adolfo Ruiz Cortines', 'Acaponeta']
#['Acatlán de Juárez', 'Adolfo Ruiz Cortines', 'Acaponeta', 'Acatic', 'Acapulco de Juárez', 'Acajete', 'Acatzingo', 'Acala', 'Acanceh', 'Acayucan', 'Acatlán de Osorio', 'Acuitlapilco', 'Actopan', 'Acámbaro', 'Abasolo']
#['Acajete', 'Acayucan', 'Acala', 'Acanceh', 'Actopan', 'Acámbaro', 'Acatlán de Juárez', 'Acaponeta', 'Adolfo Ruiz Cortines', 'Abasolo', 'Acatic', 'Acapulco de Juárez', 'Acatlán de Osorio', 'Acuitlapilco', 'Acatzingo']

# %%
