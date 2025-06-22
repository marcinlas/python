''' Napisz funkcję big_five(n), która za pomocą znaku '#' narysuje wielką,
cyfrową piątkę o szerokości n (patrz wzorcowy wynik).

KOD DO ZMIANY:
def big_five(n):
    print("#"*n)
    for i in range(n):
        print("#")
    print("#"*n)
    for i in range(n):
        print(" "*n + "#")
    print("#"*n)

'''

def big_five(n):
    print("#"*n)
    for i in range(n):
        print("#")
    print("#"*n)
    for i in range(n):
        print(" "*n + "#")
    print("#"*n)

# testowane przypadki:
big_five(4)

# źródło --> https://www.umiemyinformatyke.pl/interaktywne-python-edycja-programow/68