def piramide_num(a, b):
    if a < b:
        lista = list(range(a, b + 1))
        listaInvertida = list(range(a, b))[::-1]
        piramide = lista + listaInvertida
        return piramide

    else:
        lista = list(range(a, b))
        listaInvertida = list(range(b, a + 1))[::-1]
        listaNegativa = listaInvertida[-3]
        piramide = lista + listaInvertida + listaNegativa
        return listaNegativa

print(piramide_num(-3, 6))
