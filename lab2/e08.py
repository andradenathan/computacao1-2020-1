from math import ceil

# EXERCÍCIO 08
def rodoviaria(pessoas):
    """
    Calcula pelas regras rodoviárias a quantidade de carros necessários para uma viagem, sendo que
    em cada carro o máximo de pessoas sendo transportadas são 5
    :param pessoas: int, float -> Capacidade máxima de pessoas = 5
    :return:
    """
    return ceil(pessoas / 5)

print(rodoviaria(55))