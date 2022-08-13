respuesta = "s"
while respuesta == "s":
    print("Ingresar primer numero")
    num1 = int(input())
    print("Ingresar segundo numero")
    num2 = int(input())
    print("***Selecionar operecion***")
    print("1 - suma")
    print("2 - resta")
    print("3- multiplicacion")
    print("4 - division")
    operacion = int(input())

    if operacion == 1:
        print("La suma es: ", num1, "+", num2, "=", num1 + num2)
    if operacion == 2:
        print("La resta es: ", num1, "-", num2, "=", num1 - num2)
    if operacion == 3:
        print("La multiplicacion es: ", num1, "*", num2, "=", num1 * num2)
    if operacion == 4:
        print("La division es: ", num1, "/", num2, "=", num1 / num2)
    print("Desea continuar si(s) o No(N)")
    respuesta = input()