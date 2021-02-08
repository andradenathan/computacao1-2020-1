def melhor_volta(matriz):
    """
    Dada 10 voltas de uma corrida de Kart para cada 6 corredores, transforma uma matriz 6 x 10 e calcula
    de quem foi a melhor volta da prova contendo seu tempo e em qual volta.
    :param matriz: list -> list
    :return: tuple -> tuple
    """
    menor_tempo = volta = vencedor = 1000
    for v in range(0, len(matriz)):
        for t in range(0, len(matriz[v])):
            if min(matriz[v][t], menor_tempo) == matriz[v][t]:
                menor_tempo = min(matriz[v][t], menor_tempo)
                vencedor = v + 1
                volta = t + 1

    return vencedor, menor_tempo, volta
