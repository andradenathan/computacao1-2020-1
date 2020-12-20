from math import pi


def quadrante(angulo, graus):
    """
    Define um quadrante dado dois parâmetros, seu ângulo em radiano ou em graus e um parâmetro para checar se é Verdadeiro (para graus) ou Falso (para radianos).

    :param angulo: int, float -> int, float
    :param graus: bool
    :return: int
    """

    anguloEmGraus = angulo % 360
    anguloEmRad = angulo % (2 * pi)

    if graus:
        if anguloEmGraus <= 90:
            return 1

        elif anguloEmGraus <= 180:
            return 2

        elif anguloEmGraus <= 270:
            return 3

        elif anguloEmGraus <= 360:
            return 4

    else:
        if anguloEmRad <= pi/2:
            return 1

        elif anguloEmRad <= pi:
            return 2

        elif anguloEmRad <= (3 * pi)/2:
            return 3

        elif anguloEmRad <= 2 * pi:
            return 4
