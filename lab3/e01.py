def valorAbsoluto(numero):
    """
    Verifica se um número é maior ou menor que zero e caso seja menor retorna o seu módulo
    :param numero: int, float
    :return: int, float
    """

    if numero < 0:
        return numero * (-1)

    else:
        return numero

print(valorAbsoluto(3) == abs(3j))
