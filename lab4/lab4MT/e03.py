from math import floor

def recursiva(s):
    """
    Pega um caractere de string e retorna sua metade, a string inteira e a outra metade da mesma.
    :param s: str -> str
    :return: str -> str
    """
    meio = floor(len(s) / 2)
    return s[:meio] + s + s[meio:]