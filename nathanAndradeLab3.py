from nathanAndradeLab2 import delta

# EXERCÍCIO 01
def valorAbsoluto(numero):
    """
    Verifica se um número é maior ou menor que zero e caso seja menor retorna o seu módulo
    :param numero: int, float
    :return: int, float
    """
    if numero < 0:
        return numero * (-1)

    else:
        return numero

# EXERCÍCIO 02
def valoresReaisEq2Grau(a, b, c):
    """
    Verifica a quantidade de raízes de uma equação do segundo grau de acordo com o valor
    de um dado delta
    :param a: int
    :param b: int
    :param c: int
    :return: str
    """
    if delta(a, b, c) > 0:
        return 'Há duas raízes reais na equação'

    elif delta(a, b, c) < 0:
       return 'Não há raízes na equação'

    else:
        return 'Há uma raíz na equação'

# EXERCÍCIO 03
def mensagem(texto, n):
    """
    Envia uma mensagem dado um texto e quantas vezes esta mensagem será repetida
    :param texto: str
    :param n: int
    :return: str
    """
    return str(texto) * n

# EXERCÍCIO 04
def data(dia, mes, ano):
    """
    Informa a data desejada por um usuário através de um valor inteiro e retorna formatado
    em uma string com o padrão "DD/MM/AAAA".
    Se uma dos parâmetros da data for menor ou igual a 0, retornará a data do dia que esse
    algoritmo foi escrito
    :param dia: int
    :param mes: int
    :param ano: int
    :return: str
    """
    if dia or mes or ano <= 0:
        return 'Data: ' + str(13)+str('/')+str(12)+str('/')+str(2020)

    else:
        return 'Data: ' + str(dia)+str('/')+str(mes)+str('/')+str(ano)

# EXERCÍCIO 05
def funcaoMatematica(y, x):
    """
    De acordo com uma função matemática pré estabelecida, verifica as condições
    de existência nos pontos y e x dessa função. Se retornar True, significa que os pontos
    estão nessa função. False significa que os pontos não condizem com a lei de formação.
    :param y: int, float
    :param x: int, float
    :return: bool
    """
    if 0 < x <= 2:
        return y == x

    elif 2 <= x <= 3.5:
        return y == 2

    elif 3.5 < x <= 5:
        return y == 3

    elif x > 5:
        return y == x ** 2 - 10 * x + 28

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

# SAÍDAS DAS QUESTÕES

# EXERCÍCIO 01
# valorAbsoluto(3) == abs(3j)

# EXERCÍCIO 02
# valoresReaisEq2Grau(1, 2, 5)

# EXERCÍCIO 04
# data(25, 12, 2020)

# EXERCÍCIO 05
# funcaoMatematica(4, 6)

# EXERCÍCIO 06
# salarioLiquido(2000)

