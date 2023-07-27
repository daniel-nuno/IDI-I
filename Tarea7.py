# %%
import pandas as pd
import numpy as np
from math import factorial
from statistics import stdev

# %%
# condiciones de función de energia:
#   1.- tiene que pasar por todas las ciudades
#   3.- no repetirse la ciudad
#   4.- donde inicia tiene que terminar
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
    return  T0 / (1 + t)

# %%
df_ciudades = pd.read_excel('C:/Users/nuno/Downloads/SA2.xlsx', sheet_name='54c_test', index_col=0)
lista_ciudades = list(df_ciudades.index.values)


# %%
####111####
lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 20
configuration_limit = 100000
epochs = 10
cicle_limit = configuration_limit / repetitions / epochs
T0 = 1000

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    T0 = T0 * 0.9
    t = 0

    while t < cicle_limit:

        for _ in range(epochs):
            ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
            delta_x = prime_x - initial_x
            q = np.exp(-delta_x / temperature_function(T0, t))
            p = np.random.uniform()
            if p < q:
                initial_x = prime_x.copy()
                mejor_ruta_ciudades = ciudades_prime_x.copy()
            count_rutas = count_rutas + 1
        
        t = t + 1

    lista_mejores_rutas.append(mejor_ruta_ciudades)
    lista_mejores_distancias.append(initial_x)


print('revisando', count_rutas, 'rutas')
# la temperatura disminuye cada ciclo por 0.9%, para calcular la temperatura inicial del la mejor distancia:
# lista_mejores_distancias.index(min(lista_mejores_distancias))
print('Temperatura inicial,', T0 / (0.9** ( repetitions - (lista_mejores_distancias.index( min( lista_mejores_distancias))+1))), '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(min(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estándar de los ciclos es', round(stdev(lista_mejores_distancias), 2))

# %%
####222####
def temperature_function(T0, t):
    return  T0 / np.log(1 + t)

lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 10
configuration_limit = 10000
epochs = 10
cicle_limit = configuration_limit / repetitions / epochs
T0 = 200

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    t = 0

    while t < cicle_limit:

        for _ in range(epochs):
            ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
            delta_x = prime_x - initial_x
            q = np.exp(-delta_x / temperature_function(T0, t))
            p = np.random.uniform()
            if p < q:
                initial_x = prime_x.copy()
                mejor_ruta_ciudades = ciudades_prime_x.copy()
            count_rutas = count_rutas + 1
        
        t = t + 1

    lista_mejores_rutas.append(mejor_ruta_ciudades)
    lista_mejores_distancias.append(initial_x)


print('revisando', count_rutas, 'rutas')
# la temperatura disminuye cada ciclo por 0.9%, para calcular la temperatura inicial del la mejor distancia:
# lista_mejores_distancias.index(min(lista_mejores_distancias))
print('Temperatura inicial,', T0, '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(min(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estándar de los ciclos es', round(stdev(lista_mejores_distancias), 2))

# %%
####333####
def temperature_function(T0, t, k):
    return  (k**t) * T0

lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 10
configuration_limit = 10000
epochs = 5
cicle_limit = configuration_limit / repetitions / epochs
T0 = 200
k=0.9

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    t = 0

    while t < cicle_limit:

        for _ in range(epochs):
            ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
            delta_x = prime_x - initial_x
            q = np.exp(-delta_x / temperature_function(T0, t, k))
            p = np.random.uniform()
            if q < p:
                initial_x = prime_x.copy()
                mejor_ruta_ciudades = ciudades_prime_x.copy()
            count_rutas = count_rutas + 1
        
        t = t + 1

    lista_mejores_rutas.append(mejor_ruta_ciudades)
    lista_mejores_distancias.append(initial_x)


print('revisando', count_rutas, 'rutas')
# la temperatura disminuye cada ciclo por 0.9%, para calcular la temperatura inicial del la mejor distancia:
# lista_mejores_distancias.index(min(lista_mejores_distancias))
print('Temperatura inicial,', T0, '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(max(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(max(lista_mejores_distancias))] )
print('la desviación estándar de los ciclos es', round(stdev(lista_mejores_distancias), 2))
# %%
####444####
# condiciones de función de energia:
#   1.- tiene que pasar por todas las ciudades
#   3.- no repetirse la ciudad
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
    
    return ciudades_visitadas, distancia

def temperature_function(T0, t):
    return  T0 / (1 + t)

lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 10
configuration_limit = 10000
epochs = 5
cicle_limit = configuration_limit / repetitions / epochs
T0 = 200

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    t = 0

    while t < cicle_limit:

        for _ in range(epochs):
            ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))
            delta_x = prime_x - initial_x
            q = np.exp(-delta_x / temperature_function(T0, t))
            p = np.random.uniform()
            if p < q:
                initial_x = prime_x.copy()
                mejor_ruta_ciudades = ciudades_prime_x.copy()
            count_rutas = count_rutas + 1
        
        t = t + 1

    lista_mejores_rutas.append(mejor_ruta_ciudades)
    lista_mejores_distancias.append(initial_x)


print('revisando', count_rutas, 'rutas')
# la temperatura disminuye cada ciclo por 0.9%, para calcular la temperatura inicial del la mejor distancia:
# lista_mejores_distancias.index(min(lista_mejores_distancias))
print('Temperatura inicial,', T0, '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(min(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estándar de los ciclos es', round(stdev(lista_mejores_distancias), 2))

# %%
####555####
def funcion_energia_tsp(df_distancias, list_ciudades, ciudad_inicial, ciudad_final):
    # condiciones de función de energia:
    #   1.- tiene que pasar por todas las ciudades
    #   3.- no repetirse la ciudad
    #   4.- puedes decidir ciudad inicial y final
    #   5.- no regresa al inicio
    list_ciudades_tmp = list_ciudades[:]
    ciudad_actual = ciudad_inicial
    ciudades_visitadas = [ciudad_inicial]
    list_ciudades_tmp.remove(ciudad_inicial)
    list_ciudades_tmp.remove(ciudad_final)
    distancia = 0

    for _ in range(len(list_ciudades_tmp)):
        siguiente_ciudad = np.random.choice(list_ciudades_tmp, size = 1)[0]
        distancia = distancia + df_distancias.at[ciudad_actual, siguiente_ciudad]
        ciudad_actual = siguiente_ciudad
        ciudades_visitadas.append(siguiente_ciudad)
        list_ciudades_tmp.remove(siguiente_ciudad)
    
    distancia = distancia + df_distancias.at[ciudad_actual, ciudad_final]
    ciudades_visitadas.append(ciudad_final)

    return ciudades_visitadas, distancia

def temperature_function(T0, t):
    return  T0 / (1 + t)

lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 5
configuration_limit = 10000
epochs = 10
cicle_limit = configuration_limit / repetitions / epochs
T0 = 200

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values), 'Copenhagen', 'Lynge')[1]
    t = 0

    while t < cicle_limit:

        for _ in range(epochs):
            ciudades_prime_x, prime_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values), 'Copenhagen', 'Lynge')
            delta_x = prime_x - initial_x
            q = np.exp(-delta_x / temperature_function(T0, t))
            p = np.random.uniform()
            if p < q:
                initial_x = prime_x.copy()
                mejor_ruta_ciudades = ciudades_prime_x.copy()
            count_rutas = count_rutas + 1
        
        t = t + 1

    lista_mejores_rutas.append(mejor_ruta_ciudades)
    lista_mejores_distancias.append(initial_x)


print('revisando', count_rutas, 'rutas')
# la temperatura disminuye cada ciclo por 0.9%, para calcular la temperatura inicial del la mejor distancia:
# lista_mejores_distancias.index(min(lista_mejores_distancias))
print('Temperatura inicial,', T0, '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(min(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estándar de los ciclos es', round(stdev(lista_mejores_distancias), 2))
# %%
