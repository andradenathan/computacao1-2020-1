# Laboratório 1

# EXERCÍCIO 01
def areaRetangulo(a, b):
    # Calcula a área do retângulo dado seus dois lados
    x = a * b
    return print(f'A área do retângulo é: {x}m²')

# EXERCÍCIO 02
def areaCubo(c):
    # Calcula a área de um cubo que tem c por aresta
    A = 6 * (c ** 2)
    return print(f'A área do cubo é: {A}m²')

# EXERCÍCIO 03
def areaCoroaCircular(r1, r2):
    # Calcula a área da coroa circular dado r1 e r2
    Acc = 3.14 * (r1 ** 2 - (r2 ** 2))
    return print(f'A área da coroa circular é {Acc}m²')

# EXERCÍCIO 04
def media():
    # Calcula a média de dois números e retorna printando na tela os seus valores
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    media = (n1 + n2) / 2

    return print(f'A média de {n1} e {n2} é: {media}')

# EXERCÍCIO 05
def funcaoSegundoGrau():
    # Calcula a solução de uma função do segundo grau dado seus valores a, b, c e sua abscissa
    print('FUNÇÃO DO SEGUNDO GRAU')
    print('ax² + bx + c = 0')

    a = float(input('Digite o parâmetro a da função: '))
    b = float(input('Digite o parâmetro b da função: '))
    c = float(input('Digite a constante c da função: '))
    x = float(input('Digite um valor para a abscissa: '))

    solution = a * (x ** 2) + (b * x) + c

    return print(f'A solução da função f(x) = {a} x ({x})² + {b} x {x} + {c} é:\n'
                 f'{solution}')

# EXERCÍCIO 06
def mediaPonderada():
    # Cálculo da média ponderada de um estudante durante seus 4 bimestres
    # O peso das notas estão relacionados diretamente com os respectivos bimestres

    bim01 = float(input('Digite a nota do 1º bimestre: '))
    bim02 = float(input('Digite a nota do 2º bimestre: '))
    bim03 = float(input('Digite a nota do 3º bimestre: '))
    bim04 = float(input('Digite a nota do 4º bimestre: '))
    denominador = 10 # 1 + 2 + 3 + 4 = 10

    mediaPond = ((bim01 * 1) + (bim02 * 2) + (bim03 * 3) + (bim04 * 4)) / denominador

    return print(f'A média ponderada do estudante é: {mediaPond}')

# EXERCÍCIO 07

# EXERCÍCIO 08
def gorjeta(conta):
    # Função que calcula e retorna o quanto um garçom receberia de gorjeta dado o
    # valor da conta do restaurante

    gorjetaGarcom = conta * (10 / 100)

    return print(f'Valor da conta: R${conta}\n'
                 f'Gorjeta para o garçom: R${gorjetaGarcom}')

# EXERCÍCIO 09
def gorjeta2():
    # Calcula a gorjeta de um garçom dado o valor da conta e a gorjeta definida pela legislação
    conta = float(input('Digite o valor da conta: R$ '))
    gorjeta = float(input('Digite o valor da gorjeta em % (Ex: 10%): '))

    gorjetaGarcom = conta * (gorjeta / 100)

    return print(f'Valor da conta R${conta}\n'
                 f'Valor da gorjeta R${gorjetaGarcom}')

# EXERCÍCIO 10
def saldoFinal():
    # Calcula o valor total de uma conta dado seu valor inicial, taxa de juros em % e o núm de meses
    saldoInicial = float(input('Digite o valor da conta inicial: R$ '))
    numMeses = float(input('Número de meses: '))
    juros = float(input('Taxa de juros mensal em %: '))
    taxaJuros = juros / 100

    saldoTotal = saldoInicial * (1+(taxaJuros * numMeses))

    return print(f'Saldo inicial: R${saldoInicial:.2F}\n'
                 f'Número de meses: {numMeses}\n'
                 f'Taxa de juros: {taxaJuros}%\n'
                 f'Saldo final da conta: R${saldoTotal:.2F}')

# EXERCÍCIO 11

# <-- SAÍDAS DAS FUNÇÕES -->

# EXERCÍCIO 01
# areaRetangulo(5, 7)
# areaRetangulo(15, 2)
# areaRetangulo(500, 700)
# areaRetangulo(5, 0)

# EXERCÍCIO 02
# areaCubo(3)

# EXERCÍCIO 03
# areaCoroaCircular(2, 1)
# areaCoroaCircular(15, 5)
# areaCoroaCircular(100, 0)

# EXERCÍCIO 04
# media()

# EXERCÍCIO 05
# funcaoSegundoGrau()

# EXERCÍCIO 06
# mediaPonderada()

# EXERCÍCIO 07
#

# EXERCÍCIO 08
# gorjeta(valorDaConta)

# EXERCÍCIO 09
# gorjeta2()

# EXERCÍCIO 10
# saldoFinal()

# EXERCÍCIO 11
#