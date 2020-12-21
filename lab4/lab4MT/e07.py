def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    ax1, ay1 = x_inf_esq1, y_inf_esq1
    ax2, ay2 = x_sup_dir1, y_inf_esq1
    ax3, ay3 = x_sup_dir1, y_sup_dir1
    ax4, ay4 = x_inf_esq1, y_sup_dir1

    bx1, by1 = x_inf_esq2, y_inf_esq2
    bx2, by2 = x_sup_dir2, y_inf_esq2
    bx3, by3 = x_sup_dir2, y_sup_dir2
    bx4, by4 = x_inf_esq2, y_sup_dir2


# segunda etapa - calculo do resultado
    if ax1 == bx1 and ay1 == by1 or ax1 == bx2 and ay1 == by2 or ax1 == bx3 and ay1 == by3 or ax1 == bx4 and ay1 == by4:
        return True

    elif ax2 == bx1 and ay2 == by1 or ax2 == bx2 and ay2 == by2 or ax2 == bx3 and ay2 == by3 or ax2 == bx4 and ay2 == by4:
        return True

    elif ax3 == bx1 and ay3 == by1 or ax3 == bx2 and ay3 == by2 or ax3 == bx3 and ay3 == by3 or ax3 == bx4 and ay3 == by4:
        return True

    elif ax4 == bx1 and ay4 == by1 or ax4 == bx2 and ay4 == by2 or ax4 == bx3 and ay4 == by3 or ax4 == bx4 and ay4 == by4:
        return True

    elif bx1 < ax1 < bx2 and by1 < ay1 < by2 or bx2 < ax1 < bx3 and by2 < ay1 < by3 or bx3 < ax1 < bx4 and by3 < ay1 < by4 or bx4 < ax1 < bx1 and by4 < ay1 < by1 or bx1 < ax1 < bx3 and by1 < ay1 < by3 or bx2 < ax1 < bx4 and by2 < ax1 < by4:
        return True

    elif bx1 < ax2 < bx2 and by1 < ay2 < by2 or bx2 < ax2 < bx3 and by2 < ay2 < by3 or bx3 < ax2 < bx4 and by3 < ay2 < by4 or bx4 < ax2 < bx1 and by4 < ay2 < by1 or bx1 < ax2 < bx3 and by1 < ay2 < by3 or bx2 < ax2 < bx4 and by2 < ax2 < by4:
        return True

    elif bx1 < ax3 < bx2 and by1 < ay3 < by2 or bx2 < ax3 < bx3 and by2 < ay3 < by3 or bx3 < ax3 < bx4 and by3 < ay3 < by4 or bx4 < ax3 < bx1 and by4 < ay3 < by1 or bx1 < ax3 < bx3 and by1 < ay3 < by3 or bx2 < ax3 < bx4 and by2 < ax3 < by4:
        return True

    elif bx1 < ax4 < bx2 and by1 < ay4 < by2 or bx2 < ax4 < bx3 and by2 < ay4 < by3 or bx3 < ax4 < bx4 and by3 < ay4 < by4 or bx4 < ax4 < bx1 and by4 < ay4 < by1 or bx1 < ax4 < bx3 and by1 < ay4 < by3 or bx2 < ax4 < bx4 and by2 < ax4 < by4:
        return True

    else:
        return False



print(colisao((0, 0, 1, 1), (0, 0, 1, 1)), 'True')
print(colisao((0, 0, 1, 1), (2, 2, 3, 3)), 'False')
print(colisao((6, 5, 8, 7), (6, 2, 7, 5)), 'True')
print(colisao((4, 8, 9, 9), (2, 1, 9, 5)), 'False')
print(colisao((1, 5, 4, 8), (5, 6, 8, 9)), 'False')
print(colisao((0, 0, 2, 2), (1, 1, 3, 3)), 'True')
print(colisao((5, 5, 7, 7), (6, 3, 8, 8)), 'True')