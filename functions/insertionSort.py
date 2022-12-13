def insertionsort(vectorins):
    """Esta función ordenara el vector que le pases como argumento con
    el Método Insertion Sort"""

    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con inserción es:", vectorins)

    largo = 0  # Establecemos un contador del largo

    for i in vectorins:
        largo += 1  # Obtenemos el largo del vector

    # Recorremos la lista de 1 hasta el largo del vector
    for i in range(1, largo):

        elemento = vectorins[i]

        # Movemos los elementos de vectorins[0...i-1], que son mayores que el elemento
        # a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < vectorins[j]:
            vectorins[j+1] = vectorins[j]
            j -= 1
        vectorins[j+1] = elemento
    print("El vector ordenado con inserción es: ", vectorins)
