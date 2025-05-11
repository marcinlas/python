''' Napisz funkcję multiples(k, n), która wypisze n pierwszych wielokrotności liczby k.


KOD DO ZMIANY:
def multiples(k, n):
    print()
'''

w = 0

def multiples(k, n):
    print([k*i for i in range(1, n+1)])


# testowane przypadki:
multiples(4, 8)

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-for/100