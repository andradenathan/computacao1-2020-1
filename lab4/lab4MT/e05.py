def diff_datas(data1, data2):
    """
    Função desenvolvida a fim de calcular quantos dias se passaram de uma data inicial até uma data final.
    :param data1: int -> int (d1 = dia inicial, m1 = mês inicial, y1 = ano inicial)
    :param data2: int -> int (d2 = dia final, m2 = mês final, y2 = ano final)
    :return: int, int
    """
    d1, m1, y1 = data1.split('/')
    d2, m2, y2 = data2.split('/')

    dataFinal = ((int(y2) * 365) + (int(m2) * 30) + int(d2)) - ((int(y1) * 365) + (int(m1) * 30) + int(d1))

    return dataFinal


print(diff_datas(('10/11/1984'), ('7/4/2009')))



