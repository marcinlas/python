''' Napisz funkcję near_fifty(n), która zdecyduje, czy podana
liczba n znajduje się 'blisko' liczby 50 albo 150 (jest maksymalnie
o 10 większa albo mniejsza).

KOD DO ZMIANY:
def near_fifty(n):
    return False
'''

def near_fifty(n):
    if (n>=40 and n<=60) or (n>=140 and n <=160):
        return not False
    else:
        return False

# testowane przypadki:
print(near_fifty(48))
print(near_fifty(68))
print(near_fifty(120))
print(near_fifty(160))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/32