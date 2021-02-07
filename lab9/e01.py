def multiplica_matriz(numero):
    """
    Dado um número qualquer multiplica este número por cada posição de uma matriz.
    :param numero: int -> int
    :return: list -> list
    """
    matriz = [[1, 1, 1], [1, 1, 1]]

    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            matriz[lin][col] *= numero

    return matriz




