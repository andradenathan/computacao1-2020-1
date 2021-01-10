def zodiacoChines(ano):
    """
    Dado um ano de nascimento, retorna aproximadamente o ano chinês  que essa pessoa nasceu.
    :param ano: int -> int
    :return: str -> str
    """
    anoChines = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre'
                 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

    return anoChines[ano % 12]
