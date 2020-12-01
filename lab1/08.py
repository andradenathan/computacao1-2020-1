def gorjeta():
    # Função que calcula e retorna o quanto um garçom receberia de gorjeta dado o
    # valor da conta do restaurante

    conta = int(input('Valor da conta a ser paga em R$: '))
    gorjetaGarcom = conta * (10/100)

    return print(f'Valor da conta: R${conta}\n'
                 f'Gorjeta para o garçom: R${gorjetaGarcom}')

gorjeta()