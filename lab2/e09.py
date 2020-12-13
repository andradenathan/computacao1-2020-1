# EXERCÍCIO 09

def comprimentoCirculo(r):
    """Calcula o comprimento do círculo dado seu raio
    :param r: int, float -> raio do círculo
    :return:
    """
    return 2 * 3.14 * r

def corrida(r, dist):
    """
    Calcula quantos metros foram percorridos por um atleta dado o raio da pista e a distância que o mesmo percorreu
    :param r: int, float -> Raio da pista
    :param dist: int, float -> Distância percorrida
    :return: int, float -> Distância percorrida na pista
    """
    return dist / comprimentoCirculo(r)

print(corrida(15, 200))