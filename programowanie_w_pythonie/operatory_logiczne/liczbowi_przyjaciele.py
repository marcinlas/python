''' Napisz funkcję friends(x, y), która cofnie True, jeżeli jedna z liczb jest dokładnie o
jeden większa niż druga.

KOD DO ZMIANY:
def friends(x, y):
    return y == x + 1
'''

def can_visit(x, y, z):
    return x%7 == 0 or y%7 == 0 or z%7 == 0

# testowane przypadki:
print(friends(3, 4))
print(friends(5, 8))
print(friends(7, 6))


# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/63