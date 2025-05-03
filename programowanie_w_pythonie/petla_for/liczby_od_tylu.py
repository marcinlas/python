''' Napisz funkcję reverse_numbers(n), która wypisze liczby od 1 do n od tyłu.

KOD DO ZMIANY:
def reverse_numbers(n):
    for i in range(n):
        print(i)
'''

def reverse_numbers(n):
    for i in range(n, 0, -1):
        print(i)

# testowane przypadki:
reverse_numbers(8)

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-for/56