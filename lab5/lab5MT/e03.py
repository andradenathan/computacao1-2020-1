def intercala(lista1, lista2):
    """
    Dada duas listas, essa função gera uma nova lista contendo todos os valores das duas
    listas de forma intercalada.
    :param lista1: list -> list
    :param lista2: list -> list
    :return: list -> list
    """
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3
