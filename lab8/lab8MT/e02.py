def qtd_divisores(n):
    """
    Calcula a quantidade de divisores que um número pode ter.
    :param n:
    :return:
    """
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return divisores
