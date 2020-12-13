# Decomposições de Funções

# Funções
def pi():
    "Retorna o valor de PI com precisão de duas casas decimais"
    return 3.14

def areaCirculo(r):
    "Calcula a área de um círculo de raio r"
    return pi() * r ** 2

def areaCoroa(r1, r2):
    "Calcula a área da coroa de dois circulos concentricos, dado seus dois raios tal que r1 > r2"
    return areaCirculo(r1) - areaCirculo(r2)

def areaRetangulo(base, altura):
    "Calcula a área do retângulo dado sua base e altura"
    return base * altura

# EXERCÍCIO 01 - CALCULAR ÁREA DE UM CILINDRO RETO
def areaLateral(r, h):
    return 2 * pi() * r * h

def areaCilindroReto(r, h):
    """Calcula a área do cilindro reto dado sua área da base e sua área lateral"""
    return 2 * (areaCirculo(r)) + areaLateral(r, h)
# EXERCÍCIO 02 - CALCULAR A ÁREA DO QUADRADO

def areaQuadrado(lado1, lado2):
    "Calcula a área do quadrado dado seus dois lados"
    return areaRetangulo(lado1, lado2)

