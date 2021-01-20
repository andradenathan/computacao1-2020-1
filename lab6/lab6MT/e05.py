from math import ceil

def acima_da_media(lista_notas):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = ceil(sum(lista_notas) / len(lista_notas))
    lista_notas.append(media)
    organizaLista = sorted(lista_notas)
    indiceMedia = organizaLista.index(media)

    if media not in organizaLista:
        lista_notas.append(media)

    return organizaLista[indiceMedia + 1:]