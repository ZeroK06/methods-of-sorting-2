from random import sample
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorheap = sample(lista, 8)


def heapsort(vectorheap):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Heap Sort"""

    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con heap es:", vectorheap)

    largo = 0  # Establecemos un contador del largo

    for _ in vectorheap:
        largo += 1  # Obtenemos el largo del vector

    # Para amontonar la subparte a partir de i.
    # n es el tamaño del montón.
    def amontonar(vectorheap, n, i):
        mas_largo = i  # Tomamos i como el más grande
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < n and vectorheap[i] < vectorheap[izq]:
            mas_largo = izq

        # Ver si existe la subparte de i correctamente y
        # si es mayor que i
        if der < n and vectorheap[mas_largo] < vectorheap[der]:
            mas_largo = der

        if mas_largo != i:
            vectorheap[i], vectorheap[mas_largo] = vectorheap[mas_largo], vectorheap[i]
            # Cambiar el origen, si es necesario
            # amontonar el origen.
            amontonar(vectorheap, n, mas_largo)

    def heap(vectorheap):

        n = largo
        # Crear un montón maximo
        for i in range(n//2 - 1, -1, -1):
            amontonar(vectorheap, n, i)

        # Extraer elementos uno a uno
        for i in range(n-1, 0, -1):
            vectorheap[i], vectorheap[0] = vectorheap[0], vectorheap[i]
            # Intercambio
            amontonar(vectorheap, i, 0)

    heap(vectorheap)
    print("El vector ordenado con heap es:", vectorheap)


heapsort(vectorheap)
