# LABORATÓRIO 3 MACHINE TEACHING

# EXERCÍCIO 01
def classificacao(C, Ce, Cs, Fv, Fe, Fs):
    """
    Dado o número de vitórias, empates e saldo de gols de cada time verifica a posição deles
    na tabela do campeonato e retorna o time que está melhor classificado de acordo com as
    seguintes condições:
    # 1. Cada vitória equivale a 3 pontos, cada empate equivale a 1 ponto
    # 2. Se os times estiverem com a mesma pontuação, o saldo de gols difere o melhor time
    :param C: int -> Número de vitórias do Cormengo
    :param Ce: int -> Número de empates do Cormengo
    :param Cs: int -> Saldo de gols do Cormengo
    :param Fv: int -> Número de vitórias do Flaminthians
    :param Fe: int -> Número de empates do Flaminthians
    :param Fs: int -> Saldo de gols do Flaminthians
    :return: str
    """
    pontosCor = (C * 3) + Ce
    pontosFla = (Fv * 3) + Fe

    if pontosCor == pontosFla:
        if Cs > Fs:
            return 'Cormengo'

        elif Fs > Cs:
            return 'Flaminthias'

        elif Fs == Cs:
            return 'Empate'

    else:
        if pontosFla > pontosCor:
            return 'Flaminthias'

        else:
            return 'Cormengo'

print(classificacao(11, 13, -8, 10, 12, -9))