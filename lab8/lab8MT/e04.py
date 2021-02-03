def soma_h(n):
    """
    Dado um número N faz a somatória de uma sequência e retorna este valor reduzido para duas casas decimais.
    :param n: int -> int
    :return: float -> float
    """
    acumulador = 0
    for i in range(1, n + 1):
        H = 1 / i
        acumulador += H

    return round(acumulador, 2)
