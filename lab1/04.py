def media():
    # Calcula a média de dois números e retorna printando na tela os seus valores
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    media = (n1 + n2) / 2

    return print(f'A média de {n1} e {n2} é: {media}')

media()
