import re

while True:
    error = 0

    usuario = input("Nombre de usuario ")
    pass1 = input("contrasena ")
    pass2 = input("repite contrasena ")

    if len(usuario) < 8 or len(usuario) > 12:
        print("la longitud del usuario no es correcta")
        error = 1
    if len(pass1) < 10:
        print("la longitud de la contrasena no es correcta")
        error = 1
    if not re.search('[0-9]', pass1):
        print("la contrasena tiene que tener al menos un numero")
        error = 1
    if pass1 != pass2:
        print("las contrasenas no son iguales")
        error = 1

    if error == 0:
        print("OK")
        break