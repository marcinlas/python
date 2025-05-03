''' Czarownica chce przygotować eliksir miłości. Do przygotowania potrzebuje
5 łez feniksa i róg jednorożca. Jeżeli nie ma rogu jednorożca, może użyć 3 ogonków
fioletowych prosiaczków. W takim przypadku wystarczą jej tylko 3 łzy feniksa.
Napisz funkcję magic_test(tears, horns, tails), która dla podanej liczby łez (tears),
rogów (horns) i ogonków (tails) zdecyduje, czy czarownica może przygotować eliksir.

KOD DO ZMIANY:
def magic_test(tears, horns, tails):
    return False
'''

def magic_test(tears, horns, tails):
    # Przepis 1: róg + 5 łez
    if tears >= 5 and horns >= 1:
        return True
    # Przepis 2: 3 łzy + 3 ogonki (niezależnie, czy róg jest czy nie)
    if tears >= 3 and tails >= 3:
        return True
    # W przeciwnym razie – nie można przygotować eliksiru
    return False

# testowane przypadki:
print(magic_test(4, 1, 3))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/64