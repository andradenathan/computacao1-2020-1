def ultrapassaPopAB():
    popA = 80000
    popB = 200000
    anos = 0
    while popA < popB:
        popA *= 1.03
        popB *= 1.015
        anos += 1

    return anos

def crescimentoPop(popA, popB, txA, txB):
    if popA < popB and txA <= txB:
        return -1

    anos = 0
    while popA < popB:
        popA = popA + popA * (txA/100)
        popB = popB + popB * (txB/100)
        anos += 1
    return anos
