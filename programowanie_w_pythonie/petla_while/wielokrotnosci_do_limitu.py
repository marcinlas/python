''' Napisz funkcję multiples(n, limit),
która wypisze wielokrotności liczby n mniejsze niż limit.


KOD DO ZMIANY:
def multiples(n, limit):
    print(n)

'''

def multiples(n, limit):
    for i in range(n, limit, n):
        print(i)


# testowane przypadki:
multiples(7, 85)


# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-while/117