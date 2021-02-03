def soma_fatorial(n):
    """
    Calcula o fatorial de um número n.
    :param n: int -> int
    :return: int -> int
    """
    fat = 1
    soma = 0
    for i in range(1, n + 1):
        fat *= i
        soma += fat

    return soma
