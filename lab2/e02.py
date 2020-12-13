from math import sqrt

# EXERCÍCIO 02 - a
def delta(a, b, c):
    """
    Calcula o delta de uma função do segundo grau e retorna a solução do polinômio
    Para delta > 0 entrar em números reais, é necessário que b² > a * c
    :param a: int, float
    :param b: int, float
    :param c: int, float
    :return: int, float
    """
    discriminante = (b ** 2) - 4 * (a * c)

    return discriminante

def raizPositiva(a, b, c):
    """
    Calcula a raíz positiva de uma equação do segundo grau dado a, b e c
    :param a: int, float
    :param b: int, float
    :param c: int, float
    :return: int, float
    """
    x1 = b * (-1) + sqrt(delta(a, b, c)) / 2 * a
    return x1

def raizNegativa(a, b, c):
    """
    Calcula a raíz negativa de uma equação do segundo grau dado a, b, e c
    :param a:
    :param b:
    :param c:
    :return:
    """
    x2 = b * (-1) - sqrt(delta(a, b, c)) / 2 * a
    return x2