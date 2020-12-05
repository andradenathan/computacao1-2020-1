# EXERCÍCIO 03 - b
def nTermos(A1, n, r):
    """
    Função helper que calcula a quantidade de termos de uma PA
    :param A1: int, float -> Termo inicial
    :param n:  int, float -> Quantidade de termos
    :param r:  int, float -> Razão da PA
    :return:  int, float
    """
    An = A1 + (n - 1) * r
    termos = An / A1
    return termos

# EXERCÍCIO 03 - c
def somatoriaPa(A1, An):
    """
    Função helper que calcula a somatória de uma P.A dado seu termo inicial, termo final e a razão
    mas sem o conhecimento de quantos termos essa P.A tem
    :param A1: int, float -> termo inicial da PA
    :param An: int, float -> termo final da PA
    :param r: int, float -> razão da PA
    :return: int, float
    """
    somatoria = (A1 + An) / 2

    return somatoria

def progressaoAritmetica(A1, An, n, r):
    """
    Calcula a somatória da P.A sabendo o seu valor inicial e final, a sua razão e a qtd de termos
    dessa P.A.
    :param A1: int, float -> Valor inicial
    :param An: int, float -> Valor final
    :param n: int, float -> Número de termos
    :param r: int, float -> Razão da P.A.
    :return: int, float
    """
    return somatoriaPa(A1, An) * nTermos(A1, n, r)