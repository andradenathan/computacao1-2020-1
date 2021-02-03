from math import factorial

def soma():
    """
    Realiza a soma de uma fração com um número inteiro sobre um número fatorial menos os valores seguintes de sua
    sequência. O numerador diminui enquanto o denominador fatorial aumenta.
    :param n:
    :return:
    """
    numerador = 11
    fracaoPositiva = 0
    fracaoNegativa = 0
    for s in range(1, 11):
        numerador -= 1
        divisor = factorial(s)
        fracao = (numerador / divisor)
        if s % 2 == 0:
            fracaoPositiva -= fracao

        else:
            fracaoNegativa += fracao

    return round(fracaoNegativa + fracaoPositiva, 2)


print(soma())