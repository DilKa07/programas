print("Ingresar la nota 1")
nota1 = int(input())
print("Ingresar la nota 2")
nota2 = int(input())
print("Ingresar la nota 3")
nota3 = int(input())
promfinal = (nota1 + nota2 + nota3)/3
print("El promedio final es: ", promfinal)

# num4 = int(input("Ingresar el cuarto numero"))

if promfinal >= 10.5:
    print("Esta Aprobado")
else:
    print("Es Desaprobado")