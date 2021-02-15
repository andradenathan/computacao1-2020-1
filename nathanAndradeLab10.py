from random import randint

# EXERCÍCIO 01
def serie():
    """
    Dada uma lista de números tais números gerados aleatoriamente, verifica quantas vezes este número se repete em
    sequência na lista.
    :return: int
    """
    a = int(input('Digite um número inicial para rodar o dado: '))
    b = int(input('Digite um número final para rodar o dado: '))
    lista_numerica = []
    ocorrencia = 0
    i = 0
    j = -1
    while i < b:
        numero = randint(a, b)
        lista_numerica.append(numero)
        if lista_numerica[i] == lista_numerica[j]:
            ocorrencia += 1

        i += 1
        j += 1

    return ocorrencia

# EXERCÍCIO 02
def main():
    """
    Programa principal que relaciona todas as outras chamadas de funções. Aqui acontece a interação com o usuário
    para realizar cálculos matemáticos de algumas questões já determinadas.
    :return: float -> float
    """
    a = int(input('Digite um número a: '))
    b = int(input('Digite um número b: '))
    c = int(input('Digite um número c: '))
    opcao = int(input('[1] -> Calcula área do trapézio\n'
                      '[2] -> Calcula o quadrado dos números a, b e c\n'
                      '[3] -> Calcula a média aritmética entre\n'
                      '[4] -> Calcula a soma dos inteiros de a até b com uma variação igual a c\n'
                      '[Aviso] -> Outro número qualquer encerra o programa\n'
                      'Digite sua opção: '))

    if opcao == 1:
        return area_trapezio(a, b, c)

    if opcao == 2:
        return quadrado(a, b, c)

    if opcao == 3:
        return media_aritmetica(a, b, c)

    if opcao == 4:
        return soma_inteiros(a, b, c)

    else:
        return 'Programa encerrado.'


def area_trapezio(B, b, h):
    """
    Calcula a área do trapézio dada suas bases e altura.
    :param B: float -> float
    :param b: float -> float
    :param h: float -> float
    :return: float -> float
    """
    area = ((B + b) * h) / 2
    return area


def quadrado(a, b, c):
    """
    Recebe três valores e multiplica por eles mesmos.
    :param a: int -> int
    :param b: int -> int
    :param c: int -> int
    :return: int -> int
    """
    return a * a, b * b, c * c


def media_aritmetica(a, b, c):
    """
    Faz a soma aritmética entre três números.
    :param a: int -> int
    :param b: int -> int
    :param c: int -> int
    :return: int -> int
    """
    media = (a + b + c) / 3
    return media


def soma_inteiros(a, b, c):
    """
    Calcula a soma dos inteiros de a até b variando de c em c.
    :param a: int -> int
    :param b: int -> int
    :param c: int -> int
    :return: int -> int
    """
    for i in range(a - 1, b, c):
        a += i

    return a

# EXERCÍCIO 03
def interacao():
    matriz = []
    while True:
        nome = str(input('Nome: '))
        registro = str(input('Registro: '))
        setor = str(input('Setor: '))
        telefone = str(input('Telefone: '))
        matriz += [nome, registro, setor, telefone],
        pausar = str(input('Deseja continuar adicionando? Não -> Termina o programa: '))[0].upper()

        if pausar == 'N':
            area = str(input('Digite o setor que você está buscando: '))
            return busca(area, matriz)

def busca(area, matriz):
    """
    Busca um usuário baseado na sua área dentro da empresa.
    :param area: str -> str
    :param matriz: list -> list
    :return: list -> list
    """
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)

    return resultado


#serie() #EXERCÍCIO 01
#main() #EXERCÍCIO 02
#interacao() #EXERCÍCIO 03
