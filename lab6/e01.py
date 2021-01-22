def criar(nome, telefones='', email='', instagram='', dados=[]):
    """
    Cria uma lista de dados de um usuário para o aplicativo dos contatinhosApp.
    :param nome: str -> str
    :param telefones: list -> list
    :param email: str -> str
    :param instagram: str -> str
    :param dados: list -> list
    :return: list -> list
    """
    dados.append(nome)
    dados.append([telefones])
    dados.append(email)
    dados.append(instagram)

    return dados


def atualizar(dados = [], indice = int, novosDados = str):
    """
    Atualiza dados de um usuário a cada chamada dessa mesma função. Nessa chamada, deve-se passar o dado que quer atualizar,
    o indíce que esse dado se encontra e o novo dado que deseja inserir no lugar do dado anterior.
    :param dados: list -> list
    :param indice: int -> int
    :param novosDados: str -> str
    :return: bool -> bool
    """
    if indice <= 3 and indice != 1:
        if indice == 0:
            dados.insert(0, novosDados)
            dados.pop(1)
            return True

        elif indice == 2:
            dados.insert(2, novosDados)
            dados.pop(0)
            return True

        elif indice == 3:
            dados.insert(3, novosDados)
            dados.pop(0)
            return True

    else:
        if indice == 1:
            dados.append(novosDados)
            if novosDados == dados[1]:
                dados.pop(0)
                return True

        else:
            return False