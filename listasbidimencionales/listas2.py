m = []
n = int(input("Ingrsar el total de filas y columnas de la matriz: "))
for i in range(n):
    m.append([]):
    for j in range(n):
        m[i].append(int(input("Ingresar el valior de fila" + str(i+1) + "columnas" + str(j+1) + ":")))
print("")
for