from random import randint

def jogaDados():
    """
    Joga dois dados e conta quantas rodadas estes dois dados foram jogados
    até os valores destes dados forem iguais.
    :return: int -> int
    """
    contador = 0
    while True:
        dado1 = randint(1, 8)
        dado2 = randint(1, 8)
        contador += 1

        if dado1 == dado2:
            break

    return contador
