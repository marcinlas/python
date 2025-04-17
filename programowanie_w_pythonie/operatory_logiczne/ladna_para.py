''' Krzysztof zdecydował, że para liczb naturalnych jest ładna,
jeżeli jedna z nich jest parzysta, a druga nieparzysta.
Napisz funkcję nice(a, b), która sprawdzi, czy podana para a, b jest ładna.

KOD DO ZMIANY:
def nice(a, b):
    return False
'''

def nice(a, b):
    if (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):
        return True
    else:
        return False

# testowane przypadki:
print(nice(3, 5))
print(nice(2, 6))
print(nice(1, 6))
print(nice(3, 3))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/41