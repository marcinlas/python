''' Przekształć przygotowaną funkcję count_zeros(n) w taki sposób,
aby wypisywała liczbę zer w zapisie liczby n.
Przygotowana wersja wypisuje poszczególne cyfry.

KOD DO ZMIANY:
def count_zeros(n):
    while n > 0:
        print(n % 10)
        n = n // 10
'''

def count_zeros(n):
    while n > 0:
        print(n % 10)
        n = n // 10

# testowane przypadki:
count_zeros(105401230)


# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-while/120