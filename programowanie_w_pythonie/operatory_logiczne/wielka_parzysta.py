''' Napisz funkcję big_even(a, b), która cofnie True dokładnie wtedy,
kiedy większa z liczb a, b będzie parzysta.

KOD DO ZMIANY:
def big_even(a, b):
    return False
'''

def big_even(a, b):
    if a>b and a%2 == 0:
        if b>a and b%2 == 0:
            return False
    else:
        return True

# testowane przypadki:
print(big_even(2, 5))
print(big_even(2, 4))


# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/60