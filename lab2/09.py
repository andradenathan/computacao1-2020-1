# EXERCÍCIO 09

def comprimentoCirculo(r):
    """Calcula o comprimento do círculo dado seu raio
    :param r: int, float -> raio do círculo
    :return:
    """
    return 2 * 3.14 * r

def corrida(r, dist):
    return print(f'Foi percorrido {dist / comprimentoCirculo(r):.3F}m')

corrida(15, 200)