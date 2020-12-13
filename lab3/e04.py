def data(dia, mes, ano):
    """
    Informa a data desejada por um usuário através de um valor inteiro e retorna formatado
    em uma string com o padrão "DD/MM/AAAA".
    Se uma dos parâmetros da data for menor ou igual a 0, retornará a data do dia que esse
    algoritmo foi escrito
    :param dia: int
    :param mes: int
    :param ano: int
    :return: str
    """

    if dia or mes or ano <= 0 :
        return 'Data: ' + str(13)+str('/')+str(12)+str('/')+str(2020)

    else:
        return 'Data: ' + str(dia)+str('/')+str(mes)+str('/')+str(ano)