from math import floor

def acima_da_media(lista):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    listaOrganizada = sorted(lista)
    indiceMedia = listaOrganizada.index(media)
    novaLista = listaOrganizada[indiceMedia + 1:].copy()

    if media in novaLista:
        del novaLista[0]

    return novaLista


print(acima_da_media([7, 0, 8, 2, 4, 9, 5, 3])) # [5, 7, 8, 9]
print(acima_da_media([0, 2, 6, 9])) #[6,9]
print(acima_da_media([8, 9, 7])) # [9]