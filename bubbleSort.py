from random import sample
from time import time
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(30000))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorbs = sample(lista, 30000)

datos = {
    "Nombre": "bubblesort",
    "numInteraciones": 0,
    "numComparaciones": 0,
    "tiempo": 0
}


def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""
    numInteraciones = 0
    numComparaciones = 0
    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar es:", vectorbs)
    n = 0  # Establecemos un contador del largo del vector

    for _ in vectorbs:
        n += 1  # Contamos la cantidad de caracteres dentro del vector

    for i in range(n-1):
        # Le damos un rango n para que complete el proceso.
        for j in range(0, n-i-1):
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1]:
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
                numComparaciones += 1
            # Se intercambian si el elemento encontrado es mayor
            # Luego pasa al siguiente
        numInteraciones += 1
    datos["numComparaciones"] = numComparaciones
    datos["numInteraciones"] = numInteraciones
    #print("El vector ordenado es: ", vectorbs)


firstTime = time()
bubblesort(vectorbs)
lastTime = time()
datos["tiempo"] = lastTime - firstTime
print(datos)
