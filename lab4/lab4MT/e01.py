def concatenacao(a, b):
    """
    Função para concatenar duas strings e retorná-las em um formato abba
    :param a: str -> str
    :param b: str -> str
    :return: str
    """
    return a + 2 * b + a

print(concatenacao('festinhas', 'duodecénio'))