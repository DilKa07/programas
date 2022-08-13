i = 0
planilla = []
numempleados = int(input("Ingresar el numero de empledos: "))
while i < numempleados:
    cod = input("Ingrese su codigo: ")
    apel = input("Ingrese su apellidos: ")
    nom = input("Ingrese su nombre: ")
    pag = int(input("Ingrese su pago: "))
    des = int(input("Ingrese su descuento: "))
    total = pag - des
    registro = "E-"+cod + " " + apel + " " + nom + " " + str(pag) + " " + str(des) + " " + str(total)
    planilla.append(registro)
    i += 1
for x in planilla:
    print(x)