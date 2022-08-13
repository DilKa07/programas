import array as arr
from random import randint
a = arr.array("i", [])
contador1 = 0
contador2 = 0
for i in range(0, 200):
    a.append(randint(18, 60))
    if a[i] <= 30:
        contador1 += 1
    if a[i] >= 31 and a[i] <=60:
        contador2 += 1
print("Nueno array generado aleatoreamente")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
print(len(a))
print("Hay " +str(contador1) + " edades entre 18 a 30")
print("Hay " +str(contador2) + " edades entre 31 a 60")
