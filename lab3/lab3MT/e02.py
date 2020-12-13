# LABORATÓRIO 3 MACHINE TEACHING

# EXERCÍCIO 02
def competicao(competidor, qtdPapel, qtdFolha):
    """
    Calcula se a quantidade de folhas para uma competição de avião dado um número de
    competidores, quantidades de papéis e quantidades de folhas a serem distribuidas
    retorna se é suficiente ou não as folhas para todos

    :param competidores: int -> Número de competidores do campeonato
    :param qtdPapel: int -> Quantidade de papeis especiais comprados para o campeonato
    :param qtdFolha: int -> Quantidade de folhas que cada competidor terá direito
    :return:
    """
    if qtdPapel - (competidor * qtdFolha) > 0 or qtdPapel - (competidor * qtdFolha) == 0:
        return 'Suficiente'

    else:
        return 'Insuficiente'