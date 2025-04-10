''' Józek chce kupić lody, ale nie wie, czy starczy mu pieniędzy. Napisz funkcję icecream_test(money, price), która dla
podanej kwoty (money) i ceny lodów (price) zdecyduje, czy może Józek może kupić lody.

KOD DO ZMIANY:
def icecream_test(money, price):
    return True
'''

def icecream_test(money, price):
    return money >= price

# testowane przypadki:
print(icecream_test(20, 10))
print(icecream_test(100, 40))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/63