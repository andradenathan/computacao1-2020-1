def meiaEntrada(idade, carteira):
    if carteira == True:
        return True
    else:
        if idade > 65 or idade < 21:
            return True

def meiaEntrada2(idade, carteira):
    if carteira == True:
        return True
    elif idade >= 65 and idade <= 21:
        return True
    else:
        return True

def meiaEntrada3(idade, carteira):
    if not carteira:
        return idade >= 65 or idade <= 21
    else:
        return False


def meiaEntrada4(idade, carteira):
    if not carteira:
        return idade >= 65 or idade <= 21
    else:
        return carteira

def meiaEntrada5(idade, carteira):
    if not(idade >= 65 or idade <= 21):
        return carteira
    else:
        return True

def meiaEntrada6(idade, carteira):
    return idade >= 65 or idade <=21 or carteira