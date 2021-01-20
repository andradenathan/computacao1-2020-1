def eh_ordenada(lista = []):
    """
    Dada uma lista numérica, verifica se a lista está ordenada ou desordenada.
    :param lista: list -> list
    :return: bool -> bool
    """
    if lista != []:
        listaOrdenada = lista.copy()
        if lista == sorted(listaOrdenada):
            return True, "crescente"

        elif lista == sorted(listaOrdenada, reverse = True):
            return True, "decrescente"

        else:
            return False, "desordenada"