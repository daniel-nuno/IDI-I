# %%
import pandas as pd
import numpy as np
from math import factorial
from statistics import stdev

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

# %%
lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 100
configuration_limit = round(factorial(7) / 2 * 0.01 , 0)

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    T0 = 1000
    t = 0
    epochs = 1

    while t < configuration_limit:

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


print('revisando ', configuration_limit, 'rutas', 'en ', repetitions, 'ciclos')
print('Temperatura inicial ', T0, '. repeticiones montecarlo, ', epochs, '. t, ', t)
print('el resultado es: ', min(lista_mejores_distancias))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estandar de los ciclos es', stdev(lista_mejores_distancias))



# %%
####################### 20 ciudades
#######################
df_ciudades = pd.read_excel('C:/Users/nuno/Downloads/probarSimAnn.xlsx', sheet_name='20c', index_col=0)
lista_ciudades = list(df_ciudades.index.values)

# %%
lista_mejores_rutas = []
lista_mejores_distancias = []
count_rutas = 0
repetitions = 30
T0 = 1500

for _ in range(repetitions):
    initial_x = funcion_energia_tsp(df_ciudades, list(df_ciudades.index.values))[1]
    T0 = T0 * 0.9
    t = 0
    epochs = 50

    while temperature_function(T0, t) > (T0 * 0.15):

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
print('Temperatura inicial,', T0*0.9**(lista_mejores_distancias.index(min(lista_mejores_distancias))+1), '. Repeticiones montecarlo,', epochs, '. Y t,', t)
print('el resultado es: ', round(min(lista_mejores_distancias), 2))
print('con la ruta ', lista_mejores_rutas[lista_mejores_distancias.index(min(lista_mejores_distancias))] )
print('la desviación estandar de los ciclos es', round(stdev(lista_mejores_distancias), 2))
# %%
# el resultado es:  1782.5
# con la ruta  ['Atengo', 'Antonio Escobedo', 'Ahualulco de Mercado', 'Amatitán', 'Atenguillo',
#  'Ameca', 'Acatlán de Juárez', 'Ahuatlán', 'Atequiza', 'Atemajac de Brizuela', 'Arandas', 'Allende',
# 'Atotonilco el Alto', 'Ahuisculco', 'Altus Bosques', 'Acatic', 'Ajijic', 'Amacueca', 'Atacco', 'Alista']

# el resultado es:  1781.27
# con la ruta  ['Altus Bosques', 'Ameca', 'Atengo', 'Alista', 'Amacueca', 'Atacco',
# 'Atemajac de Brizuela', 'Acatlán de Juárez', 'Acatic', 'Ahuatlán', 'Allende',
# 'Atotonilco el Alto', 'Arandas', 'Ahuisculco', 'Atequiza', 'Ajijic',
# 'Amatitán', 'Antonio Escobedo', 'Atenguillo', 'Ahualulco de Mercado']

# el resultado es:  1738.72
# con la ruta  ['Arandas', 'Allende', 'Ahuatlán', 'Ajijic', 'Acatlán de Juárez',
# 'Altus Bosques', 'Alista', 'Ahuisculco', 'Atenguillo', 'Ahualulco de Mercado',
# 'Amatitán', 'Ameca', 'Antonio Escobedo', 'Atengo', 'Atacco', 'Atemajac de Brizuela',
# 'Amacueca', 'Atequiza', 'Acatic', 'Atotonilco el Alto']

#revisando 1177500 rutas
#Temperatura inicial, 7.73066281098018 . Repeticiones montecarlo, 50 . Y t, 785
#el resultado es:  1704.99
#con la ruta  ['Atacco', 'Alista', 'Amacueca', 'Atemajac de Brizuela', 'Atengo',
# 'Ajijic', 'Amatitán', 'Atenguillo', 'Ahualulco de Mercado', 'Antonio Escobedo',
# 'Ameca', 'Ahuisculco', 'Acatlán de Juárez', 'Arandas', 'Allende',
# 'Atotonilco el Alto', 'Ahuatlán', 'Altus Bosques', 'Acatic', 'Atequiza']
#la desviación estandar de los ciclos es 325.68