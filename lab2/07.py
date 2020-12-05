# EXERCÍCIO 07
def imc(altura, peso):
    """
    Calcula o índice de massa corporal dado a altura e o peso de uma pessoa
    :param altura: int, float -> Altura
    :param peso: int, float -> Peso
    :return: int, float
    """
    return peso / altura ** 2

print(imc(1.8, 80))