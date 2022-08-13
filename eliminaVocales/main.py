palabra = input("Ingresar una palabra: ")
vocales = "aeiouAEIOU"
for letra in palabra:
    if letra not in vocales:
        print(letra, end=" ")