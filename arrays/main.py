import array as arr
from random import randint
a = arr.array("i", [1, 2, 3])
print("El nuevo array creado es: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.append(19)
a.insert(1, 4)
for i in range(0, len(a)):
    print(a[i],end=" ")
print()
for i in range(0, 95):
    a.append(i)
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
numbus = int(input("Ingrese el numero que desea buscar: "))
print("El nuemro buscado esta en la posición")
print(a.index(numbus))
a = arr.array("i", [])
contador = 0
for i in range(0, 100):
    a.append(randint(0, 400))
    if a[i] <= 100:
        contador += 1
print("Nueno array generado aleatoreamente")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
print(len(a))
print("Hay " +str(contador) + " numeros menores o igual a 100")