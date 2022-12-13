from random import sample
from time import time

# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(30000))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorquick = sample(lista, 30000)

datos = {
    "Nombre": "bubblesort",
    "numInteraciones": 0,
    "numComparaciones": 0,
    "tiempo": 0
}


def quicksort(vectorquick, start=0, end=len(vectorquick) - 1):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Quick Sort"""

    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar con quick es:", vectorquick)

    def quick(vectorquick, start=0, end=len(vectorquick) - 1):

        if start >= end:
            datos["numComparaciones"] += 1
            return

        def particion(vectorquick, start=0, end=len(vectorquick) - 1):
            pivot = vectorquick[start]
            menor = start + 1
            mayor = end

            while True:
                datos["numInteraciones"] += 1
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorquick[mayor] >= pivot:
                    datos["numInteraciones"] += 1
                    mayor = mayor - 1

                # Proceso opuesto al anterior
                while menor <= mayor and vectorquick[menor] <= pivot:
                    datos["numInteraciones"] += 1
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    datos["numComparaciones"] += 1
                    vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                    # Continua el bucle
                else:
                    datos["numComparaciones"] += 1
                    # Salimos del bucle
                    break

            vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]

            return mayor

        p = particion(vectorquick, start, end)
        quick(vectorquick, start, p-1)
        quick(vectorquick, p+1, end)

    quick(vectorquick)
    #print("El vector ordenado con quick es:", vectorquick)


firstTime = time()
quicksort(vectorquick)
lastTime = time()
datos["tiempo"] = lastTime - firstTime
print(datos)

