respuesta = "s"
while respuesta == "s":
    print("Ingresar un numero")
    numero = int(input())
    i = 1
    while i <= 12:
        print(numero, " * ", i, " = ", i * numero)
        i += 1
    print("Desea continuar si(s) o No(N)")
    respuesta = input()
