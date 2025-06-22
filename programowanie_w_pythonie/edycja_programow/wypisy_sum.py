''' Napisz funkcję print_sums(n), która wypisze wszystkie sposoby,
na jakie można wyrazić podaną liczbę n jako sumę dwóch liczb naturalnych.

KOD DO ZMIANY:
def print_sums(n):
    for i in range(n):
        print(n, "=", i, "+", i)

'''

def print_sums(n):
    for i in range(n):
        print(n, "=", i, "+", i)


# testowane przypadki:
print_sums(13)

# źródło --> https://www.umiemyinformatyke.pl/interaktywne-python-edycja-programow/45