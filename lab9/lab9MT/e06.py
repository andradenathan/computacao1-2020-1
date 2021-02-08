def ordena_por_insercao(lista):
    """
    Dada uma lista de números faz uma verificação das suas posições e se um número é maior (da esquerda para direita)
    que o anterior, realiza uma troca de posição.
    :param list: list -> list
    :return: list -> list
    """
    for i in range(0, len(lista)):
        numero = lista[i]
        j = i - 1
        while j >= 0 and numero < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = numero

    return lista

print(ordena_por_insercao([0, 2, 4, 3, 6, 7, 8, 22, 10, 35, 15, 18]))
