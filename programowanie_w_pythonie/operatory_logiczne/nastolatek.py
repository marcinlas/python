''' Przekształć podaną funkcję teenager(age) w taki sposób, żeby poprawnie oceniała, czy podana wartość age odpowiada
wieku nastolatka, czyli leży w przedziale od 13 do 19 (włącznie). Zamiast or trzeba użyć innego operatora logicznego.

KOD DO ZMIANY:
def teenager(age):
  return age > 9 or age <= 20
'''

def teenager(age):
    return age > 12 and age <= 19

# testowane przypadki:
print(teenager(10))
print(teenager(15))
print(teenager(19))
print(teenager(30))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/76