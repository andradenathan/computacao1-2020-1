def areaCoroaCircular(r1, r2):
    """Calcula a área da coroa circular dado r1 e r2
    tal que r1 > r2"""

    areaDaCoroa = 3.14 * (r1 ** 2 - (r2 ** 2))
    return print(f'A área da coroa circular é {areaDaCoroa}m²')

areaCoroaCircular(2, 1)
areaCoroaCircular(15, 5)
areaCoroaCircular(100, 0)
