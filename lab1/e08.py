def gorjeta(conta):
    """Calcula e retorna o quanto um garçom receberia de gorjeta dado o
     valor da conta do restaurante"""

    gorjetaGarcom = conta * (10/100)

    return print(f'Valor da conta: R${conta}\n'
                 f'Gorjeta para o garçom: R${gorjetaGarcom}')

gorjeta(1300)