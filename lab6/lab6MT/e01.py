def altera_frase(frase, palavra, posicao):
    """
    Altera uma frase para receber uma nova palavra em uma determinada posição. Se a palavra já existir na frase,
    o algoritmo destaca essa palavra para o usuário sem fazer alterações. Se não estiver, ele adiciona a palavra na
    posição escolhida pelo usuário.
    :param frase: str -> str
    :param palavra: str -> str
    :param posicao: int -> int
    :return: str -> str
    """

    fraseSeparada = frase.split()

    if palavra in fraseSeparada:
        indice = fraseSeparada.index(palavra)
        fraseSeparada[indice] = palavra.upper()
        novaFrase = " ".join(fraseSeparada)
        return novaFrase

    else:
        fraseSeparada.insert(posicao, palavra)
        novaFrase = " ".join(fraseSeparada)
        return novaFrase