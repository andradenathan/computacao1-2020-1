from math import hypot, dist, sin, cos, pi

# EXERCÍCIO 04 - a
def hipotenusa(catetoAd, catetoOp):
    """
    Calcula a hipotenusa do triângulo dado seus dois catetos
    :param catetoAd: int, float -> Cateto adjacente
    :param catetoOp: int, float -> Cateto oposto
    :return: int, float
    """
    return hypot(catetoAd, catetoOp)

# EXERCÍCIO 04 - b
def distAb(pontoA, pontoB):
    """
    Calcula a distância entre o ponto A e o ponto B de uma reta em um plano
    :param pontoA: int, float -> Ponto A
    :param pontoB: int, float -> Ponto B
    :return: int, float
    """
    a = [pontoA]
    b = [pontoB]

    return dist(a, b)

# EXERCÍCIO 04 - c
def perimetro(catetoAd, catetoOp):
    """
    Calcula o perímetro de um triângulo dado seus catetos e hipotenusa
    :param catetoAd: int, float -> Cateto Adjacente
    :param catetoOp: int, float -> Cateto Oposto
    :return: int, float
    """
    return catetoAd + catetoOp + hipotenusa(catetoAd, catetoOp)

def somaSinCos(angulo):
    """
    Calcula a soma do quadrado do seno com o quadrado do cosseno
    :param angulo: int -> Ângulo em graus
    :return:
    """
    return sin(angulo) ** 2 + cos(angulo) ** 2

def comprimentoCirculo(r):
    """Calcula o comprimento do círculo dado seu raio
    :param r: int, float -> raio do círculo
    :return:
    """
    return 2 * pi * r
