# EXERCÍCIO 01 - a
def valorMaxMin(num1, num2, num3):
    """Encontra valor máximo e valor mínimo através de funções nativas do Python
    :param num1: int, float
    :param num2: int, float
    :param num3: int, float
    :return: int, float
    """
    return max(num1, num2, num3), min(num1, num2, num3)

# EXERCÍCIO 01 - b
def mediaTresNumeros(n1, n2, n3):
    """Calcula a média entre três números e retorna um print da média
    :param n1: int, float
    :param n2: int, float
    :param n3: int, float
    :return int, float"""
    media = (n1 + n2 + n3) / 3

    return media

# EXERCÍCIO 01 - c
def diferencaComMedia(número1, número2, número3):
    """Calcula a diferença entre o valor máximo dado três números com a sua média
    :param número1: int, float
    :param número2: int, float
    :param número3: int, float
    :return: int, float
    """
    return max(número1, número2, número3) - mediaTresNumeros(número1, número2, número3)

# EXERCÍCIO 01 - d
def somaMenorComMedia(número1, número2, número3):
    """Calcula a média e soma com o menor número dado três valores
    :param número1: int, float
    :param número2: int, float
    :param número3: int, float
    :return: int, float
    """
    return min(número1, número2, número3) + mediaTresNumeros(número1, número2, número3)

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

# <-- SAÍDAS DAS FUNÇÕES -->
# EXERCÍCIO 01
# print(valorMaxMin(3, 4, 9))
# print(mediaTresNumeros(3, 4, 9))
# print(diferencaComMedia(3, 4, 9))
# print(somaMenorComMedia(3, 4, 10))

# EXERCÍCIO 02
# print(delta(2, 7, 2))


