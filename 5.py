import random

punkty = []
ponizej = []

for  x  in range(15):
    punkty.append(round(random.uniform(0, 50), 2))
print(punkty)
print(f"wartość minimalna: {min(punkty)}")
print(f"wartość maksymalna: {max(punkty)}")
liczba = float(input("Podaj liczbę: "))

if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Nie ma takiej liczby!")

suma = sum(punkty)
srednia = round(suma /len(punkty), 2)
print(f"Średnia ilość punktów: {srednia}")

for y in punkty:
    if y < srednia:
        ponizej.append(y)

powyzej = [y for y in punkty if y > srednia]
print(f"Osoby poniżej średniej: {ponizej}, osoby powyżej średniej: {powyzej}")
print(len(ponizej), len(powyzej))