''' Olbrzym Polikarp ma buty siedmiomilowe. Potrafi robić w nich tylko siedmiomilowe kroki. Chce odwiedzić jedną
ze swoich trzech koleżanek olbrzymek (Xenia, Yvonna, Zenobia). Olbrzymki mieszkają w odległości x, y i z mil.
Olbrzym potrzebuje funkcji can_visit(x, y, z), która zadecyduje, czy może odwiedzić przynajmniej jedną z nich
(tzn. będzie mógł pokonać odległość siedmiomilowymi krokami). Olbrzym już raz spróbował napisać funkcję,
ale nie do końca mu się to udało. Popraw ją.

KOD DO ZMIANY:
def can_visit(x, y, z):
    return x%7 == 0 and x%7 == 1 and x%7 == 2
'''

def can_visit(x, y, z):
    return x%7 == 0 or y%7 == 0 or z%7 == 0

# testowane przypadki:
print(can_visit(5, 6, 7))
print(can_visit(5, 7, 6))
print(can_visit(15, 16, 17))
print(can_visit(30, 40, 50))
print(can_visit(35, 49, 70))

# źródło --> https://www.umiemyinformatyke.pl/interaktywny-python-operatory-logiczne/63