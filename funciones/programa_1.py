def retornar_perimetro(lado):
    return lado * 4

#bloqueprincipal
lado=int(input("Ingrese el lado del cuadrado: "))
x = retornar_perimetro(lado)
print("El perimetro del cuadrado es", x)