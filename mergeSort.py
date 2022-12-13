from random import sample
from time import time

# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(30000))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectormerge = sample(lista, 30000)

datos = {
    "Nombre": "bubblesort",
    "numInteraciones": 0,
    "numComparaciones": 0,
    "tiempo": 0
}


def mergesort(vectormerge):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Merge Sort"""

    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar con merge es:", vectormerge)

    def merge(vectormerge):

        def largo(vec):
            largovec = 0  # Establecemos un contador del largovec
            for _ in vec:
                largovec += 1  # Obtenemos el largo del vector
            return largovec

        if largo(vectormerge) > 1:
            datos["numComparaciones"] += 1
            medio = largo(vectormerge)//2  # Buscamos el medio del vector

            # Lo dividimos en 2 partes
            izq = vectormerge[:medio]
            der = vectormerge[medio:]

            merge(izq)  # Mismo procedimiento a la primer mitad
            merge(der)  # Mismo procedimiento a la segunda mitad

            i = j = k = 0

            # Copiamos los datos a los vectores temporales izq[] y der[]
            while i < largo(izq) and j < largo(der):
                datos["numInteraciones"] += 1
                if izq[i] < der[j]:
                    datos["numComparaciones"] += 1
                    vectormerge[k] = izq[i]
                    i += 1
                else:
                    datos["numComparaciones"] += 1
                    vectormerge[k] = der[j]
                    j += 1
                k += 1

            # Nos fijamos si quedaron elementos en la lista
            # tanto derecha como izquierda
            while i < largo(izq):
                datos["numInteraciones"] += 1
                vectormerge[k] = izq[i]
                i += 1
                k += 1

            while j < largo(der):
                datos["numInteraciones"] += 1
                vectormerge[k] = der[j]
                j += 1
                k += 1
    merge(vectormerge)
    #print("El vector ordenado con merge es: ", vectormerge)


firstTime = time()
mergesort(vectormerge)
lastTime = time()
datos["tiempo"] = lastTime - firstTime
print(datos)
