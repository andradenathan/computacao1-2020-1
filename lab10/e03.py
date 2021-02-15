def main():
    matriz = []
    while True:
        nome = str(input('Nome: '))
        registro = str(input('Registro: '))
        setor = str(input('Setor: '))
        telefone = str(input('Telefone: '))
        matriz += [nome, registro, setor, telefone],
        pausar = str(input('Deseja continuar adicionando? Não -> Termina o programa: '))[0].upper()

        if pausar == 'N':
            area = str(input('Digite o setor que você está buscando: '))
            return busca(area, matriz)

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

main()