def busca(area, matriz):
    """
    Busca um usuário baseado na sua área dentro da empresa.
    :param area: str -> str
    :param matriz: list -> list
    :return: list -> list
    """
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if area.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)

    return resultado


print(busca('RH', [['Adalberto Ferreira', '566', 'Contabilidade', '(21) 84564-3248'], ['Juliana Vasconcelos', '465', 'RH', '(21) 3555-4552'], ['Flavia Amorim', '565', 'Contabilidade', '(21) 2134-4845']]))
