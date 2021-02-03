def lingua_p(palavra):
    minusculo = palavra.lower()
    nova_palavra = ''
    vogais = 'aeiouãéíóú'
    vogal_palavra = ''
    for p in range(0, len(palavra)):
        if minusculo[p] in vogais:
            vogal_palavra += minusculo[p]
            nova_palavra += minusculo[p] + 'p' + vogal_palavra[:2]

        else:
            nova_palavra += minusculo[p]

    return nova_palavra

print(lingua_p('advirdes'), 'apadvipirdepes')