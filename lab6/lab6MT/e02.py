def faltas(campeonato):
    """
    Dado uma partida de um campeonato a função faz a soma do total de faltas de uma partida.
    :param time1: str -> str
    :param time2: str -> str
    :param faltas: list -> list
    :return: int -> int
    """
    totFaltas = sum(campeonato[0][2] + campeonato[1][2] + campeonato[2][2])

    return totFaltas