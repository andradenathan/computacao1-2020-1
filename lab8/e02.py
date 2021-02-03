def buscar(lista, nome):
    """
    Busca um usuário a partir do seu nome registrado e adiciona em uma nova lista de contatos.
    :param lista: list -> list
    :param nome: str -> str
    :return: list -> list
    """
    contatos = []
    for l in range(0, len(lista)):
        if nome.lower() in lista[l][0].lower():
            contatos.append(lista[l])

    return contatos