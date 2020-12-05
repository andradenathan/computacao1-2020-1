from math import radians

# EXERCÍCIO 05
def setorCircular(raio, angulo=360):
    """
    Calcula a área do setor circular de uma circunferência
    :param angulo: int, float -> Ângulo da circunferência em graus
    :param raio: int, float -> Raio da circunferência
    :return:
    """
    anguloRad = radians(angulo)
    area = (raio ** 2) * anguloRad / 2
    return area
