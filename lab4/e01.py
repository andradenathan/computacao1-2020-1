def SIGA(aluno):
    """
    Sistema de Integração e Gestão de Alunos - verifica o nome do estudante, as notas das
    suas três provas durante um semestre e retorna a situação do mesmo.
    Se o estudante teve a média das três notas acima e incluindo o 5, é Aprovado. Do contrário, Reprovado.
    No final do algoritmo ele retornará uma tupla contendo o nome, a média do aluno e sua situação.
    :param aluno: str, float, float, float -> str, float, float, float
    :return: tuple
    """
    (nome, p1, p2, p3) = aluno
    media = round((p1 + p2 + p3) / 3, 1)

    if media >= 7:
        return (nome, media, "Status: Aprovado", "Parabéns!")

    elif media >= 5:
        return (nome, media, "Status: Aprovado")

    else:
        return (nome, media, "Status: Reprovado")