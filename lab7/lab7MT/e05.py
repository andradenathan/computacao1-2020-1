def fatorial(numero):
    """
    Dado um número, retorna o fatorial desse mesmo número.
    :param numero: int -> int
    :return: int -> int
    """
    contador = 1
    fat = 1

    while contador <= numero:
        fat *= contador
        contador += 1
        print(fat)

    return fat
