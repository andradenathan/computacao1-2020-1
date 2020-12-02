def mediaPonderada():
    """Cálculo da média ponderada de um estudante durante seus 4 bimestres,
    o peso das notas estão relacionados diretamente com os respectivos bimestres"""

    bim01 = float(input('Digite a nota do 1º bimestre: '))
    bim02 = float(input('Digite a nota do 2º bimestre: '))
    bim03 = float(input('Digite a nota do 3º bimestre: '))
    bim04 = float(input('Digite a nota do 4º bimestre: '))
    denominador = 10 # 1 + 2 + 3 + 4 = 10

    mediaPond = ((bim01 * 1) + (bim02 * 2) + (bim03 * 3) + (bim04 * 4)) / denominador

    return print(f'A média ponderada do estudante é: {mediaPond}')

mediaPonderada()



