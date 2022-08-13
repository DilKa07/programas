import os
def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
i = 0
totalacomulado = 0
igvacomulado = 0
factura = []
numproducto = int(input("Ingresar el numero de productos: "))
while i < numproducto:
    codigo = input("Ingrese el codigo: ")
    nompro = input("Ingresa el nombre del producto: ")
    cantidadventas = int(input("Ingresar cantidad de ventas: "))
    precio = float(input("Ingresar precio: "))
    total = round(cantidadventas * precio, 2)
    igv = round(total * 0.18, 2)
    totalacomulado = totalacomulado + total
    igvacomulado = igvacomulado + igv
    registro = "P-" + codigo + "  " + nompro + " " * (20 - len(nompro)) + str(cantidadventas) + " " * (10 - len(str(cantidadventas))) + str(precio) + " " * (10 - len(str(precio))) + str(igv) + " " * 8 + str(total)
    factura.append(registro)
    i += 1
x = 0
while x <= 10:
    print(" ")
    x += 1
print("CODIGO","NOMBRE DEL PRODUCTO","CANTIDAD","PRECIO","IGV","TOTAL")
for x in factura:
    print(x)
    print("*" * 20)
    print("Total: ", totalacomulado)
    print("IGV", round(igvacomulado, 2))