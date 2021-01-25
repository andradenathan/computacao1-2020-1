def posLetra(string, letra, numero):
    """
    Dada uma string, um número e uma letra, retorna a posição que essa letra está de acordo com a sua ocorrência.
    :param string: str -> str
    :param letra: str -> str
    :param numero: int -> int
    :return: int -> int
    """
    contador = 0
    indice = 0
    ocorrencia = 0
    lista = list(string)
    while contador < len(lista):
        if lista[indice] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return indice

        contador += 1
        indice += 1

    return -1
