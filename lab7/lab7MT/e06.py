def faltante(lista):
    """
    Dada uma lista de números, se um número não estiver dentro daquele intervalo [1, N] retorna o número que está
    faltando.
    :param lista: list -> list
    :return: int -> int
    """
    contador = 0
    listaNumeros = list(range(lista[0], len(lista) + 1))
    numero = 0

    while contador < len(lista):
        if listaNumeros[contador] not in lista:
            numero += listaNumeros[contador]


        contador += 1

    return numero

print(faltante([1, 2, 3]))