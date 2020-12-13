def funcaoMatematica(y, x):
    """
    De acordo com uma função matemática pré estabelecida, verifica as condições
    de existência nos pontos y e x dessa função. Se retornar True, significa que os pontos
    estão nessa função. False significa que os pontos não estão plotados no gráfico.
    :param y: int, float
    :param x: int, float
    :return: bool
    """
    if 0 < x <= 2:
        return y == x

    elif 2 <= x <= 3.5:
        return y == 2

    elif 3.5 < x <= 5:
        return y == 3

    elif x > 5:
        return y == x ** 2 - 10 * x + 28


print(funcaoMatematica(4, 6))








