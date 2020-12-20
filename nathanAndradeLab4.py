from math import pi

# LABORATÓRIO 4

# EXERCÍCIO 01
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

# EXERCÍCIO 02
def quadrante(angulo, graus):
    """
    Define um quadrante dado dois parâmetros, seu ângulo em radiano ou em graus e um parâmetro para checar se é Verdadeiro (para graus) ou Falso (para radianos).

    :param angulo: int, float -> int, float
    :param graus: bool
    :return: int
    """

    anguloEmGraus = angulo % 360
    anguloEmRad = angulo % (2 * pi)

    if graus:
        if anguloEmGraus <= 90:
            return 1

        elif anguloEmGraus <= 180:
            return 2

        elif anguloEmGraus <= 270:
            return 3

        elif anguloEmGraus <= 360:
            return 4

    else:
        if anguloEmRad <= pi/2:
            return 1

        elif anguloEmRad <= pi:
            return 2

        elif anguloEmRad <= (3 * pi)/2:
            return 3

        elif anguloEmRad <= 2 * pi:
            return 4


# SAÍDAS DAS QUESTÕES

# EXERCÍCIO 01
# SIGA(('Nathan', 10, 9, 10)) - Aprovado
# SIGA(('Ronald McDonalds', 1, 8, 5)) - Reprovado

# EXERCÍCIO 02
# quadrante(720, True) -> 1º Quadrante
# quadrante(3.5, False) -> 3º Quadrante