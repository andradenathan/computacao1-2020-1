def F(n):
    lista = []
    for i in range(0, 11):
        list.append(lista, i*n)
    return lista

def F2(c1, c2):
    c3 = []
    for i in c1:
        if i in c2:
            list.append(c3, i)
    return c3


def ultima_ocorrencia(frase, letra):
    i = 0
    while i < len(frase):
        if frase[i] == letra:
            pos = i
        i += 1
    return pos

def ultima_ocorrencia2(frase, letra):
    for i in range(len(frase)):
        if frase[i] == letra:
            pos = i
    return pos

#print(ultima_ocorrencia2('', 'a'))
#print(ultima_ocorrencia2(' ', 'a'))
print(ultima_ocorrencia2('abcda', 'a'))
print(ultima_ocorrencia2('jklaper', 'a'))
#print(ultima_ocorrencia2('poiuy', 'a'))
