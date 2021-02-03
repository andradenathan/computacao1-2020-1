def primo(n):
    """
    Verifica se um número é primo ou não de acordo com a quantidade de números que o divide.
    :param n:
    :return:
    """
    numerosPrimos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            numerosPrimos += 1

    if numerosPrimos == 2:
        return True

    else:
        return False

print(primo(6))
