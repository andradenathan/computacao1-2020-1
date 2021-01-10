def piramide_num(a, b):
    """
    Gera uma sequência numérica dado dois números, onde o primeiro número será o primeiro e o último da sequência,
    o maior número (número b) estará no meio e a partir deste maior, os números diminuirão até o valor do número a.
    :param a: int -> int
    :param b: int -> int
    :return: list -> list
    """
    if a < b:
        # Soma-se um no range para obter a sequência numérica + o valor que será o meio da pirâmide.
        listaA = list(range(a, b + 1))
        # A partir do meio da pirâmide, exclui o número do meio que se repetirá e inverte o restante da sequência.
        listaB = listaA[-2::-1]
        piramide = listaA + listaB
        return piramide

    if a > b:
        # Quando o a for maior que o b deve-se fazer o inverso da listaA quando o b é maior que o a.
        listaA = list(range(a, b - 1, -1))
        listaB = listaA[-2::-1]
        return listaA + listaB

    else:
        return [a if a != [] else b]

print(piramide_num(0, 0))

