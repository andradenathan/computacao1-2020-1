def funcaoSegundoGrau():
    print('FUNÇÃO DO SEGUNDO GRAU')
    print('ax² + bx + c = 0')

    a = float(input('Digite o parâmetro a da função: '))
    b = float(input('Digite o parâmetro b da função: '))
    c = float(input('Digite a constante c da função: '))
    x = float(input('Digite um valor para a abscissa: '))

    solution = a * (x ** 2) + (b * x) + c

    return print(f'A solução da função f(x) = {a} x ({x})² + {b} x {x} + {c} é:\n'
                 f'{solution}')

funcaoSegundoGrau()

