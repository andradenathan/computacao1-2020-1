from nathanAndradeLab2 import delta

def valoresReaisEq2Grau(a, b, c):
    """
    Verifica a quantidade de raízes de uma equação do segundo grau de acordo com o valor
    de um dado delta
    :param a: int
    :param b: int
    :param c: int
    :return: str
    """

    delta(a, b, c)

    if delta(a, b, c) > 0:
        return 'Há duas raízes reais na equação'

    elif delta(a, b, c) < 0:
       return 'Não há raízes na equação'

    else:
        return 'Há uma raíz na equação'


print(valoresReaisEq2Grau(1, 2, 5))