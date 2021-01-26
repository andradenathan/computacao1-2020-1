def faltante(lista):
    """
    Dada uma lista de números, se um número não estiver dentro daquele intervalo [1, N] retorna o número que está
    faltando.
    :param lista: list -> list
    :return: int -> int
    """
    contador = 0
    listaOrdenada = sorted(lista)

    while contador < len(lista):
        if contador + 1 == listaOrdenada[contador]:
            contador += 1

        else:
            return contador + 1

    return contador + 1
