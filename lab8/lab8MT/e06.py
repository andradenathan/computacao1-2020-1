def lingua_p(palavra):
    """
    Adiciona uma letra p antes da vogal de uma dada palavra.
    :param palavra: str -> str
    :return: str -> str
    """
    minusculo = palavra.lower()
    nova_palavra = ''
    vogais = 'aeiouãáéíóú'
    for p in minusculo:
        nova_palavra += p
        if p in vogais:
            nova_palavra += 'p' + p

    return nova_palavra
