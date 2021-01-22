def f(lista1):
    if len(lista1) > 2:
        lista2 = lista1
    else:
        lista2 = lista1[:]

    list.append(lista1, [3,4])
    list.append(lista1, [4,5])
    del lista1[2]
    if lista1[0] == 1:
        lista1 = lista1*2

    return lista2
