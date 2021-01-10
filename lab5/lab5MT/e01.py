def quant_palavras(frase):
    """Dada uma frase a função contará o número de palavras dentro desta frase"""
    removeSpaces = frase.strip()
    splitPhrase = removeSpaces.split()
    return len(splitPhrase)