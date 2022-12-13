from random import sample
from time import time

# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(30000))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorshell = sample(lista, 30000)

datos = {
    "Nombre": "bubblesort",
    "numInteraciones": 0,
    "numComparaciones": 0,
    "tiempo": 0
}


def shellsort(vectorshell):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Shell Sort"""

    #print("El vector a ordenar con shell es:", vectorshell)

    largo = 0

    for i in vectorshell:
        largo += 1

    distancia = largo // 2

    # Creamos un bucle según las distancias
    while distancia > 0:
        datos["numInteraciones"] += 1
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            datos["numInteraciones"] += 1
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                datos["numInteraciones"] += 1
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2  # Acotamos la distancia nuevamente y continua el ciclo
    #print("El vector ordenado con shell es: ", vectorshell)


firstTime = time()
shellsort(vectorshell)
lastTime = time()
datos["tiempo"] = lastTime - firstTime
print(datos)
