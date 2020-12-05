# EXERCÍCIO 08
def rodoviaria(pessoas):
    """
    Calcula pelas regras rodoviárias a quantidade de carros necessários para uma viagem, sendo que
    em cada carro o máximo de pessoas sendo transportadas são 5
    :param pessoas: int, float -> Capacidade máxima de pessoas = 5
    :return:
    """
    return print(f'{(pessoas / 5):.1F}')

rodoviaria(4)