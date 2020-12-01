def gorjeta2():
    conta = float(input('Digite o valor da conta: R$ '))
    gorjeta = float(input('Digite o valor da gorjeta em % (Ex: 10%): '))

    gorjetaGarcom = conta * (gorjeta / 100)

    return print(f'Valor da conta R${conta}\n'
                 f'Valor da gorjeta R${gorjetaGarcom}')

gorjeta2()