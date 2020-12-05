from math import sqrt, hypot, dist, sin, cos, pi, radians, ceil

# Laboratório 2

# EXERCÍCIO 01 - a
def valorMaxMin(num1, num2, num3):
    """Encontra valor máximo e valor mínimo através de funções nativas do Python
    :param num1: int, float
    :param num2: int, float
    :param num3: int, float
    :return: int, float
    """
    return max(num1, num2, num3), min(num1, num2, num3)

# EXERCÍCIO 01 - b
def mediaTresNumeros(n1, n2, n3):
    """Calcula a média entre três números e retorna um print da média
    :param n1: int, float
    :param n2: int, float
    :param n3: int, float
    :return int, float"""
    media = (n1 + n2 + n3) / 3

    return media

# EXERCÍCIO 01 - c
def diferencaComMedia(número1, número2, número3):
    """Calcula a diferença entre o valor máximo dado três números com a sua média
    :param número1: int, float
    :param número2: int, float
    :param número3: int, float
    :return: int, float
    """
    return max(número1, número2, número3) - mediaTresNumeros(número1, número2, número3)

# EXERCÍCIO 01 - d
def somaMenorComMedia(número1, número2, número3):
    """Calcula a média e soma com o menor número dado três valores
    :param número1: int, float
    :param número2: int, float
    :param número3: int, float
    :return: int, float
    """
    return min(número1, número2, número3) + mediaTresNumeros(número1, número2, número3)

# EXERCÍCIO 02 - a
def delta(a, b, c):
    """
    Calcula o delta de uma função do segundo grau e retorna a solução do polinômio
    Para delta > 0 entrar em números reais, é necessário que b² > a * c
    :param a: int, float
    :param b: int, float
    :param c: int, float
    :return: int, float
    """
    discriminante = (b ** 2) - 4 * (a * c)

    return discriminante
def raizPositiva(a, b, c):
    """
    Calcula a raíz positiva de uma equação do segundo grau dado a, b e c
    :param a: int, float
    :param b: int, float
    :param c: int, float
    :return: int, float
    """
    x1 = b * (-1) + sqrt(delta(a, b, c)) / 2 * a
    return x1

def raizNegativa(a, b, c):
    """
    Calcula a raíz negativa de uma equação do segundo grau dado a, b, e c
    :param a:
    :param b:
    :param c:
    :return:
    """
    x2 = b * (-1) - sqrt(delta(a, b, c)) / 2 * a
    return x2

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

# EXERCÍCIO 05
def setorCircular(raio, angulo=360):
    """
    Calcula a área do setor circular de uma circunferência
    :param angulo: int, float -> Ângulo da circunferência em graus
    :param raio: int, float -> Raio da circunferência
    :return:
    """
    anguloRad = radians(angulo)
    area = (raio ** 2) * anguloRad / 2
    return area

# EXERCÍCIO 06
def comprarBombom(valor, carteira):
    qtdBombom = carteira / valor
    return print(f'Pedrinho consegue comprar {qtdBombom} bombons')

# EXERCÍCIO 07
def imc(altura, peso):
    """
    Calcula o índice de massa corporal dado a altura e o peso de uma pessoa
    :param altura: int, float -> Altura
    :param peso: int, float -> Peso
    :return: int, float
    """
    return peso / altura ** 2

# EXERCÍCIO 08
def rodoviaria(pessoas):
    """
    Calcula pelas regras rodoviárias a quantidade de carros necessários para uma viagem, sendo que
    em cada carro o máximo de pessoas sendo transportadas são 5
    :param pessoas: int, float -> Capacidade máxima de pessoas = 5
    :return:
    """
    return print(f'{(pessoas / 5):.1F}')

# EXERCÍCIO 09
def corrida(r, dist):
    """
    Calcula quantos metros foram percorridos por um atleta dado o raio da pista e a distância que o mesmo percorreu
    :param r: int, float -> Raio da pista
    :param dist: int, float -> Distância percorrida
    :return: int, float -> Distância percorrida na pista
    """
    return print(f'Foi percorrido {dist / comprimentoCirculo(r):.3F}m')

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

# <-- SAÍDAS DAS FUNÇÕES -->
# EXERCÍCIO 01
# print(valorMaxMin(3, 4, 9))
# print(mediaTresNumeros(3, 4, 9))
# print(diferencaComMedia(3, 4, 9))
# print(somaMenorComMedia(3, 4, 10))

# EXERCÍCIO 02
# print(delta(2, 7, 2))
# print(raizPositiva(1, -5, 4))
# print(raizNegativa(1, -5, 4))

# EXERCÍCIO 03
# print(progressaoAritmetica(2, 40, 20, 2))

# EXERCÍCIO 04
# print(hipotenusa(3, 4))
# print(hipotenusa(5, 12))
# print(hipotenusa(7, 24))
# print(distAb(3, 1))
# print(distAb(255, 1000))
# print(distAb(6, 10))
# print(perimetro(3, 4))
# print(perimetro(6, 12))
# print(perimetro(5, 10))
# print(somaSinCos(45))
# print(somaSinCos(90))
# print(somaSinCos(1))
# print(comprimentoCirculo(3))
# print(comprimentoCirculo(4))
# print(comprimentoCirculo(1080))

# EXERCÍCIO 05
# print(setorCircular(120, 12))
# print(setorCircular(32, 2))
# print(setorCircular(45, 4))

# EXERCÍCIO 06
# comprarBombom(2, 50)

# EXERCÍCIO 07
# print(imc(1.8, 80))

# EXERCÍCIO 08
# rodoviaria(3)

# EXERCÍCIO 09
# corrida(15, 200)

# EXERCÍCIO 10
# fazerBolo(4, 6, 10) # deverá retornar 2 pois há a qtd. exatas dos ingredientes
# fazerBolo(4, 6, 9) # deverá retornar 1 pois há um argumento que não está exato dado o dobro de colheres ter que ser 10