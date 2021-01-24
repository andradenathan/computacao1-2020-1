def f1(palavra):
    i = 0
    while i < len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            return palavra[i]
        i += 1

    return ''
