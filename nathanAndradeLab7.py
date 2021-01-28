from random import randint

def jogaDados():
    """
    Joga dois dados e conta quantas rodadas estes dois dados foram jogados
    até os valores destes dados forem iguais.
    :return: int -> int
    """
    contador = 0
    while True:
        dado1 = randint(1, 8)
        dado2 = randint(1, 8)
        contador += 1

        if dado1 == dado2:
            break

    return contador

def buscar(lista, nome):
    """
    Busca um usuário a partir do seu nome registrado e adiciona em uma nova lista de contatos.
    :param lista: list -> list
    :param nome: str -> str
    :return: list -> list
    """
    contatos = []
    contador = 0

    while contador < len(lista):
        if nome.lower() in lista[contador][0].lower():
            contatos.append(lista[contador])

        contador += 1

    return contatos
