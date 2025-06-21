''' Napisz funkcję animals(n), która wypisze n powtórzeń słów ryba, które są przeplatane słowem rak.

KOD DO ZMIANY:
def animals(n):
    print("ryba")
'''

def animals(n):
    for i in range(n):
        print("ryba")
        if i < n - 1:
            print("rak")
    print()  # na koniec przechodzi do nowej linii

# testowane przypadki:
animals(3)

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-for/98