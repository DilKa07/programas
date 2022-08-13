def superficie_rectangulo(b, h):
    rectangulo1 = b * h
    return rectangulo1

# bloque principal
print("Primer rectangulo")
base1 = int(input("Ingrese la base del rectangulo: "))
altura1 = int(input("Ingrese la altura del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectangulo(base1, altura1))

def superficie_rectangulo2(b, h):
    rectangulo2 = b * h
    return rectangulo2


print("Segundo rectangulo")
lado1 = int(input("Ingrese el lado del rectangulo: "))
lado2 = int(input("Ingrese el ancho del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectangulo(lado1, lado2))

if superficie_rectangulo(base1, altura1) > superficie_rectangulo2(lado1, lado2):
    print("La superficie del primer rectangulo es mayor")
else:
    print("La superficie del segundo rectangulo es mayor")