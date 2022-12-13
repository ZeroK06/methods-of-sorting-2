from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorselect = sample(lista, 8)


def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar es:", vectorselect)

    largo = 0

    for _ in vectorselect:
        largo += 1  # Obtenemos el largo del vector

    for i in range(largo):

        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i
        for j in range(i+1, largo):
            if vectorselect[minimo] > vectorselect[j]:
                minimo = j

        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado es: ", vectorselect)


selectionsort(vectorselect)
