import random
a = []
filas = 5
columnas = 4
cpar = 0
for i in range(filas):
    a.append([])
    for j in range(columnas):
        a[i].append(random.randrange(100))
        if a[i][j]% 2 == 0:
            cpar = cpar + 1
            print(a)
            print("Cantidad de valores pares: ", str(cpar))