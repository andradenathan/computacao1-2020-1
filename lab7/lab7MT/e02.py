def uppCons(frase):
    """
    Dada uma frase com consoantes e vogais, transforma todas as consoantes em maiusculo enquanto as vogais ficam em
    minusculo.
    :param frase: str -> str
    :return: str -> str
    """
    contador = 0
    novaFrase = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novaFrase += frase[contador].upper()
        else:
            novaFrase += frase[contador].lower()
        contador += 1

    return novaFrase
