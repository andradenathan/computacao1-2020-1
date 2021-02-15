from random import randint

def serie():
    """
    Dada uma lista de números tais números gerados aleatoriamente, verifica quantas vezes este número se repete em
    sequência na lista.
    :return: int
    """
    a = int(input('Digite um número inicial para rodar o dado: '))
    b = int(input('Digite um número final para rodar o dado: '))
    lista_numerica = []
    ocorrencia = 0
    i = 0
    j = -1
    while i < b:
        numero = randint(a, b)
        lista_numerica.append(numero)
        if lista_numerica[i] == lista_numerica[j]:
            ocorrencia += 1

        i += 1
        j += 1

    return ocorrencia