def dist():
    """Calcula a distância que a correnteza arrasta um barco que estava atravessando um rio"""

    velBarco = float(input('Digite a velocidade do barco: '))
    velCorrenteza = float(input('Digite a velocidade da correnteza: '))
    larguraRio = float(input('Digite o tamanho da largura do rio: '))

    """Unidade da equação validada pois a velocidade da correnteza é perpendicular à velocidade do barco e 
    m/s cortará com m/s, então, só teremos m da largura do rio"""

    distancia = (velCorrenteza/velBarco) * larguraRio

    return print(f'Velocidade da correnteza: {velCorrenteza} m/s\n'
                 f'Velocidade do barco: {velBarco} m/s\n'
                 f'Largura do rio: {larguraRio} m\n'
                 f'\033[31mDistância que a correnteza arrastará o barco: {distancia:.1F} m\033[m')

dist()

