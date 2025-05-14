''' Napisz funkcję even_numbers(n), która wypisze n liczb parzystych (począwszy od dwójki).

KOD DO ZMIANY:
def even_numbers(n):
    print(2)
'''

def even_numbers(n):
    for i in range(1, n + 1):
        print(2 * i)

# testowane przypadki:
even_numbers(6)

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-for/57