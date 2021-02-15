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


main()