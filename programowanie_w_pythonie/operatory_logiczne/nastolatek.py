'''
Przekształć podaną funkcję teenager(age) w taki sposób, żeby poprawnie oceniała,
czy podana wartość age odpowiada wieku nastolatka,
czyli leży w przedziale od 13 do 19 (włącznie).
Zamiast or trzeba użyć innego operatora logicznego.
'''

def teenager(age):
    return age > 10 or age <= 20
