''' Policjant potrzebuje pomocy z wlepianiem mandatów. Poszedł do baru i
sprawdził wiek (age) obywatela oraz to, czy pije piwo (beer). Napisz funkcję
impose_fine(age, beer), która cofnie True w przypadku, kiedy obywatel jest
niepełnoletni i pije piwo.

KOD DO ZMIANY:
def impose_fine(age, beer):
    return False
'''

def impose_fine(age, beer):
    if age<=17 and beer==True:
        return not False
    else:
        return False

# testowane przypadki:
print(impose_fine(20, True))
print(impose_fine(15, False))
print(impose_fine(17, True))
print(impose_fine(57, True))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/33