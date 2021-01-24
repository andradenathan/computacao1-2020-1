def ultima_vogal(palavra):
    i = 0
    vogal = ''
    while i < len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            vogal = palavra[i]
        i += 1
    return vogal
