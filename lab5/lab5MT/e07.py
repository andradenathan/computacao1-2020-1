def colchao(medidas, H, L):
    """
    Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L.
    :param medidas: list -> list
    :param H: int -> int
    :param L: int -> int
    :return: bool -> bool
    """
    [A, B, C] = medidas
    if A and B > H and L:
        return False

    else:
        return True


print(colchao([25, 200, 220], 200, 100))

