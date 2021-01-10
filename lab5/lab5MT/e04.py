def retira_pontuacao(frase):
    """
    Dada uma frase pontuada, remove todos os pontos como travessão, vírgula, dois pontos, ponto e vírgula
    e ponto final transformando-os em um espaço.
    :param frase: str -> str
    :return: str -> str
    """
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrogacao = pontoFinal.replace('?', ' ')
    pontoExclamacao = pontoInterrogacao.replace('!', ' ')
    return pontoExclamacao
