def quem_ligou(lista, telefone):
    """
    Verifica nos dados de um usuário se um dado telefone existe nesta lista. Caso exista, retorna uma lista
    com os dados deste usuário e se não encontrar, devolve uma lista vazia.
    :param lista: list -> list
    :param telefone: str -> str
    :return: list -> list
    """
    contatos = []

    for l in range(0, len(lista)):
        for tel in range(0, len(lista[l])):
            if telefone in lista[l] and telefone != '':
                contatos.append(lista[tel])

    return contatos





