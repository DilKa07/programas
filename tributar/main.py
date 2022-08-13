edad = int(input("Ingresa tu edad: "))
ingresos = float(input("¿Cuanto es tu ingreso mensual? "))
if edad > 18 and ingresos >= 2700:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")