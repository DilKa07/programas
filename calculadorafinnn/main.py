nombrecliente = input("Ingresar el nombre del cliente: ")
fechaventa = input("Ingresar la fecha de la venta: ")
cantidadventas = int(input("Ingresar la cantidad de ventas: "))
i = 1
sumamontoventas = 0
while i <= cantidadventas:
    print("Ingresar el monto de la venta ", i, " : ")
    montoventa = float(input())
    sumamontoventas = sumamontoventas + montoventa
    i += 1
igv = sumamontoventas * 0.18
totalventa = sumamontoventas + igv
print("Señor(a): ", nombrecliente, "el monto total de la venta es:", sumamontoventas)
print("El IGV es: ", igv)
print("El total de la compra es: ", totalventa)