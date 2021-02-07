def melhor_volta(matriz):
    """
    Dada 10 voltas de uma corrida de Kart para cada 6 corredores, transforma uma matriz 6 x 10 e calcula
    de quem foi a melhor volta da prova contendo seu tempo e em qual volta.
    :param matriz:
    :return:
    """
    menor_tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor_tempo) == matriz[v][t]:
                menor_tempo = min(matriz[v][t], menor_tempo)
                vencedor = v + 1
                volta = t + 1

    return vencedor, menor_tempo, volta


print(melhor_volta([[88, 60, 62, 26, 93, 13, 74, 9, 54, 1], [43, 64, 72, 35, 2, 65, 97, 7, 57, 84], [95, 69, 76, 94, 53, 8, 75, 96, 31, 44], [36, 98, 16, 71, 59, 99, 19, 30, 46, 100], [18, 58, 49, 89, 37, 14, 82, 66, 51, 77], [85, 87, 17, 50, 67, 90, 63, 47, 22, 101]]), 'correto: ', (1, 1, 10))
print(melhor_volta([[26, 81, 39, 97, 19, 10, 51, 31, 22, 41], [15, 30, 7, 95, 5, 50, 20, 91, 56, 88], [65, 82, 87, 62, 77, 21, 3, 99, 1, 8], [92, 23, 89, 48, 38, 66, 9, 98, 83, 2], [6, 33, 16, 49, 11, 45, 12, 28, 46, 60], [68, 53, 44, 27, 42, 86, 13, 94, 4, 52]]), 'correto: ', (3, 1, 9))
print(melhor_volta([[74, 77, 57, 35, 66, 22, 46, 55, 7, 79], [20, 62, 93, 6, 67, 85, 1, 11, 49, 76], [84, 44, 87, 27, 19, 43, 56, 29, 86, 63], [12, 61, 92, 40, 8, 60, 13, 68, 23, 98], [45, 18, 65, 10, 70, 9, 69, 2, 36, 14], [94, 47, 15, 39, 91, 80, 21, 58, 48, 24]]), 'correto: ', (2, 1, 7))
print(melhor_volta([[68, 55, 47, 14, 21, 70, 59, 48, 53, 41], [82, 85, 19, 84, 87, 58, 43, 11, 12, 13], [99, 18, 66, 86, 89, 24, 27, 54, 15, 28], [49, 50, 75, 100, 76, 90, 51, 22, 26, 33], [77, 5, 46, 88, 16, 34, 32, 29, 23, 80], [44, 78, 1, 10, 45, 7, 35, 72, 8, 42]]), 'correto: ', (6, 1, 3))