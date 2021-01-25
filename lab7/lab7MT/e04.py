def repetidos(lista):
    """
    Dada uma lista numérica verifica a posição de um número e se o número antecedente a ele é ele mesmo. Caso seja,
    conta quantas vezes este número se repetiu.
    :param lista: list -> list
    :return: int -> int
    """
    indice = 0
    contador = 0
    repete = 0
    while contador < len(lista):
        if lista[indice] == lista[indice - 1]:
            repete += 1

        indice += 1
        contador += 1

    return repete

print(repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7]))