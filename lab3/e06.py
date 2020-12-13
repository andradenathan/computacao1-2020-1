# EXERCÍCIO 06 - a
def descontoImpostos(salarioBruto):
    """
    Calcula a taxa de descontos de impostos do INSS dado o salário bruto de uma pessoa
    6% - para salários até R$2.000,00.
    8% - para salários acima de R$2.000,00 até R$3.000,00
    10% - para salários acima de R$3.000,00
    :param salarioBruto: float
    :return: float
    """
    if salarioBruto <= 2000:
        return salarioBruto * 6/100

    elif 2000 < salarioBruto <= 3000:
        return salarioBruto * 8/100

    elif salarioBruto > 3000:
        return salarioBruto * 10/100

# EXERCÍCIO 06 - b
def descontosIR(salarioBruto):
    """
    Calcula a taxa de desconto do Imposto de Renda de uma pessoa dado seu salário bruto
    11% - para salários até R$3.000,00
    15% - para salários acima de R$3.000,00 até R$5.000,00
    22% - para salários acima de R$5.000,00
    :param salarioBruto: float
    :return: float
    """
    if salarioBruto <= 2500:
        return salarioBruto * 11/100

    elif salarioBruto <= 5000:
        return salarioBruto * 15/100

    elif salarioBruto > 5000:
        return salarioBruto * 22/100


# EXERCÍCIO 06 - c
def salarioLiquido(salarioBruto):
    """
    Calcula o salário líquido de uma pessoa dado seu salário bruto menos a somatória
    das taxações de impostos
    :param salarioBruto: float
    :return: float
    """
    return salarioBruto - (descontoImpostos(salarioBruto) + descontosIR(salarioBruto))
