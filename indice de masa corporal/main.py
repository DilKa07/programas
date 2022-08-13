peso = input("¿Ingresar tu peso en kg? ")
estatura = input("¿Ingresar tu estatura en metros? ")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es: " + str(imc))