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


def inverte(frase):
    """
    Dada uma frase esta função retornará a frase invertida e sem pontuações.
    Exemplo: "Nossa, como eu gosto de chocolate."
    Retorno: "chocolate de gosto eu como nossa"
    :param frase: str -> str
    :return: str -> str
    """
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin

print(inverte('Nossa, como eu gosto de chocolate.'))