''' Przekształć funkcję stars(n) w taki sposób,
żeby wypisywała n gwiazdek, i jednocześnie każda grupa pięciu gwiazdek była
oddzielona pionową kreską.

KOD DO ZMIANY:
def stars(n):
    for i in range(n):
        print("*", end="")
        if i == 5:
            print("|", end="")
    print()
'''

def stars(n):
    for i in range(n):
        print("*", end="")
        if i == 5:
            print("|", end="")
    print()

# testowane przypadki:
stars(7)
stars(15)


# źródło --> https://www.umiemyinformatyke.pl/interaktywne-python-edycja-programow/37