def conta_numero(numero, matriz):
    """
    Verifica se na matriz existe um determinado número e se existir conta quantas vezes ele se repete nesta lista.
    :param numero: int -> int
    :param matriz: list -> list
    :return: int -> int
    """
    contador = 0
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin][col] == numero:
                contador += 1

    return contador

print(conta_numero(1, [[1, 1, 0, 4], [2, 3, 4, 6], [5, 8, 0, 1]]))