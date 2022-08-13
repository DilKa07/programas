usuario = input("Ingresar el numero de usuario: ")
caracteres = len (usuario)
tipo = usuario.isalnum()
if tipo == True:
    if caracteres < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif caracteres > 12:
        print("El nombre de usuario no puede contener mas de 12 caracteres")
    else:
        print("Bienvenido", usuario)
else:
    print("El nombre de usuario puede contener solo letras y numeros")