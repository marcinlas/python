''' Przekształć funckję sequences(n) w taki sposób,
żeby wypisywała stopniowo wydłużający się ciąg pierwszych n liczb
(patrz wzorcowy wynik).

KOD DO ZMIANY:
def sequences(n):
    for i in range(n):
        for j in range(i+1):
            print(i, end=" ")
        print()


'''

def sequences(n):
    for i in range(n):
        for j in range(i+1):
            print(i, end=" ")
        print()


# testowane przypadki:
sequences(8)

# źródło --> https://www.umiemyinformatyke.pl/interaktywne-python-edycja-programow/35