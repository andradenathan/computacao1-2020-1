def g(x, y):
    acumula = 0
    for i in range(x):
        for j in range(i, y):
            acumula += y
            print(acumula)
    return acumula

#g(3, 5)

def transposta(m):
    nlin = len(m)
    ncol = len(m[0])
    ret = []
    for i in range(ncol):
        linha = nlin* [0]
        list.append(ret, linha)

    for i in range(nlin):
        for j in range(ncol):
            ret[i][j] = m[j][i]

    return ret

def somaMatrizes(A, B):
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            list.append(linha, A[i][j] + B[i][j])
        list.append(C, linha)
    return C

#print(somaMatrizes([[4, 6, 7, 0]], [[1, 2, 3, 4]]))

def maiorLinha(matriz):
    somas = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
        list.append(somas, soma)
    maior = max(somas)
    pos = list.index(somas, maior)
    return matriz[pos], maior

#print(maiorLinha([[1, 2, 4, 6, 7, 10, 225]]))

def cr(notas):
    soma = 0
    peso = 0
    for disciplina in notas:
        soma += disciplina[0] * disciplina[1]
        peso = peso + disciplina[0]

    CR = soma / peso
    return CR

print(cr([[6, 8]]))