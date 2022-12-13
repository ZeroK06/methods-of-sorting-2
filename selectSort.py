from random import sample
from time import time

# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(30000))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorselect = sample(lista, 30000)

datos = {
    "Nombre": "bubblesort",
    "numInteraciones": 0,
    "numComparaciones": 0,
    "tiempo": 0
}


def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""
    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar es:", vectorselect)

    largo = 0

    for _ in vectorselect:
        largo += 1  # Obtenemos el largo del vector

    for i in range(largo):
        datos["numInteraciones"] += 1
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i
        for j in range(i+1, largo):
            datos["numInteraciones"] += 1
            if vectorselect[minimo] > vectorselect[j]:
                datos["numComparaciones"] += 1
                minimo = j

        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
        # Repetimos el proceso hasta terminar
    #print("El vector ordenado es: ", vectorselect)


firstTime = time()
selectionsort(vectorselect)
lastTime = time()
datos["tiempo"] = lastTime - firstTime
print(datos)
