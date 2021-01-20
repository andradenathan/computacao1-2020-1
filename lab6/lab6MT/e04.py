def maiores(lista, n):
    """
    Dada uma lista de números e um número n, gera uma nova lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    :param lista_numeros:
    :param n: int -> int
    :return: int -> int
    """
    list(lista)
    lista.append(n)
    listaOrganizada = sorted(lista)
    indiceN = listaOrganizada.index(n)
    if n not in listaOrganizada:
        lista.append(n)

    return listaOrganizada[indiceN + 1:]