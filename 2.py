import random

zestaw_1 = []
n = int(input("Podaj rozmiar lista: "))
for i in range(n):
    x = random.randint(1, 10)
    zestaw_1.append(x)
print(zestaw_1)

n = int(input("Podaj rozmiar lista: "))
zestaw_2 = [random.randint(5, 15) for i in range(n)]
print(zestaw_2)

liczba = int(input("Podaj liczbę: "))
if liczba  in  zestaw_1:
    print("Liczna z zestawu pierwszego.")
elif liczba in zestaw_2:
    print("Liczna z zestawu drugiego.")
else:
    print("Liczba nie występuje w żadnym z zestawów!")