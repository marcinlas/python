''' Napisz funkcję big_even(a, b), która cofnie True dokładnie wtedy,
kiedy większa z liczb a, b będzie parzysta.

KOD DO ZMIANY:
def big_even(a, b):
    return False
'''

def big_even(a, b):
    if a>b and a%2 == 0 or b>a and b%2 == 0:
        return not False
    else:
        return False

# testowane przypadki:
print(big_even(2, 5))
print(big_even(2, 4))
print(big_even(7, 3))
print(big_even(8, 6))
print(big_even(8, 5))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/60