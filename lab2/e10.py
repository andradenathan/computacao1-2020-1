# EXERCÍCIO 10
def fazerBolo(A=2, B=3, C=5):
    """
    Calcula a quantidade máxima de bolos dada a quantidade exata de ingredientes que
    o João deseja fazer
    :param A: int -> Xícaras de farinha de trigo
    :param B: int -> Ovos
    :param C: int -> Colheres de sopa de leite
    :return: int -> Quantidade máxima de bolos que podem ser feitas
    """
    return min(A // 2, B // 3, C // 5)

print(fazerBolo(4, 6, 10))








