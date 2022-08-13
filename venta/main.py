print("Nombre del cliente")
cliente = input()
print(cliente)
print("Ingresar fecha")
fecha1 = input()
print(fecha1)
i = 1
sumaventas = 0
while respuesta1 == "s":
    print("INgresar el monto de venta")
    monto1 = float(input())
    IGV = 1.18
    print("***RESUMEN***")
    print("Monto:", monto1)
    print("IGV:", IGV)
    print(cliente, "el total de la venta es" , monto1, "*", IGV, "=", monto1 * IGV)
    monto2 = float(input())
