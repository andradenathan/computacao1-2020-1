def diferenca(q, n):
    """Calcula o erro de aproximação (a diferença) entre uma sequência infinita e uma sequência finita
    de uma PG, sendo que 0 <= q < 1"""

    erro = 1 + (1 - (q ** n)) / 1 - q
    return print(f'O erro entre o valor da soma de uma PG infinita e dos seus n primeiros termos é: {erro}')

diferenca(0.5, 3)