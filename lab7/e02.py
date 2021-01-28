def buscar(lista, nome):
    """
    Busca um usuário a partir do seu nome registrado e adiciona em uma nova lista de contatos.
    :param lista: list -> list
    :param nome: str -> str
    :return: list -> list
    """
    contatos = []
    contador = 0

    while contador < len(lista):
        if nome.lower() in lista[contador][0].lower():
            contatos.append(lista[contador])

        contador += 1

    return contatos


print(buscar([['Nathan', 20], ['Gabriel Augusto', 20]], 'than'))