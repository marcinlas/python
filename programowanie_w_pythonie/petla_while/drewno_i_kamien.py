''' Marcin ma mniej drewna niż kamieni.
Za jednym razem wydobywa 2 drewna i 1 kamień. Będzie wydobywał,
dopóki nie będzie miał tyle drewna, ile kamieni.
Napisz funkcję materials(d, k),
która dla podanej liczby drewna i kamieni wypisze przebieg
wydobycia (patrz przykład).


KOD DO ZMIANY:
def materials(d, k):
    print("D = ", d, ", K = ", k, sep="")


'''

def materials(d, k):
    print("D = ", d, ", K = ", k, sep="")
    while d != k:
        materials(d + 2, k + 1)
        break



# testowane przypadki:
materials(5, 9)



# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-while/121
