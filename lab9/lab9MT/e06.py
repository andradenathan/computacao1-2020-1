def ordena_por_insercao(lista):
    """
    Dada uma lista de números faz uma verificação das suas posições e se um número é maior (da esquerda para direita)
    que o anterior, realiza uma troca de posição.
    :param list: list -> list
    :return: list -> list
    """
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j - 1]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]

    return lista