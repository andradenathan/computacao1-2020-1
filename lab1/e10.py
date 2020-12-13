def saldoFinal():
    """Função que calcula o saldo final de uma conta dado seu valor inicial, taxa de juros em %
    e a quantidade de meses que a mesma será paga"""

    saldoInicial = float(input('Digite o valor da conta inicial: R$ '))
    numMeses = float(input('Número de meses: '))
    juros = float(input('Taxa de juros mensal em %: '))
    taxaJuros = juros / 100

    saldoTotal = saldoInicial * (1+(taxaJuros * numMeses))

    return print(f'Saldo inicial: R${saldoInicial:.2F}\n'
                 f'Número de meses: {numMeses}\n'
                 f'Taxa de juros: {taxaJuros}%\n'
                 f'Saldo final da conta: R${saldoTotal:.2F}')

saldoFinal()