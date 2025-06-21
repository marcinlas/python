''' Przekształć funkcję products(n) w taki sposób, żeby wypisywała tabliczkę mnożenia
pierwszych n liczb (patrz wzorcowy wynik).

KOD DO ZMIANY:
def products(n):
    for row in range(n):
        for col in range(n):
            print(row + col, end=" ")
        print()
'''

def products(n):
    for row in range(n):
        for col in range(n):
            print(row + col, end=" ")
        print()

# testowane przypadki:
products(8)

# źródło --> https://www.umiemyinformatyke.pl/interaktywne-python-edycja-programow/36