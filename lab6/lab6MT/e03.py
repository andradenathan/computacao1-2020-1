def insere(lista_numero, n):
    """
    Dada uma lista numérica, adiciona um número n e reorganiza a lista colocando o n em uma posição de acordo com o seu
    valor em módulo.
    :param lista_numero: list -> list
    :param n: int -> int
    :return: list -> list
    """
    list(lista_numero)
    lista_numero.append(n)
    listaOrganizada = sorted(lista_numero)

    return listaOrganizada

print(insere([1, 4, 5, 9, 1000, 22], 3))