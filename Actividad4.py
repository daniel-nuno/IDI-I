# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Genere una lista L con los resultados de emular 1000 veces el experimento de obtener la suma de dos dados.
# Suponga que los dados están cargados y el 5 tiene el doble de probabilidades que los demás. ¿Qué porcentaje de los resultados fue 10?

L = np.random.choice(range(1,7), size = 1000, p = [1/7, 1/7, 1/7, 1/7, 2/7, 1/7]) + np.random.choice(range(1,7), size = 1000, p = [1/7, 1/7, 1/7, 1/7, 2/7, 1/7])
print (np.array([L == 10]).sum() / 1000)
# %%
#Genere una lista M con los resultados de emular las respuestas aleatorias de 1000 exámenes de 8 preguntas verdadero-falso.
#   ¿Cuál fue el promedio de calificación sobre 100?
M = np.random.binomial(8, 0.5, 1000)
M.mean() * 100 / 8
# %%
# Se sabe que por un crucero pasan en promedio 20 coches por minuto.
# Emule aleatoriamente los resultados de tomar mediciones cada minuto durante una hora.
# ¿Cuál fue el mayor y el menor valor obtenido?
coches = np.random.poisson(20,1000)
plt.hist(coches, density=True)
# %%
coches.max()
coches.min()
# %%
# El coeficiente intelectual (IQ) es un estimador de la inteligencia general.
# Se distribuye normalmente con una media de 100 y desviación estándar de 15. 
# Genere una lista Q que emule los IQ de una muestra aleatoria de 500 personas.
# Si se considera a una persona superdotada si su IQ es igual o mayor a 130,
# ¿cuántos superdotados se obtuvieron en la simulación?
Q = np.random.normal(100, 15, 500)
print(np.array([Q > 130]).sum())
# %%
