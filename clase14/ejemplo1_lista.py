def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

def mayor(lista):
    may = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may

def menor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men

# BLOQUE PRINCIPAL DEL PROGRAMA

listavalores = [10, 56, 23, 120, 94]
print("La lista completa es: ")
print(listavalores)
print("La suma de todos sus elementos es: ", sumarizar(listavalores))
print("El mayor valor es: ", mayor(listavalores))
print("El menos valor de la lista es: ", menor(listavalores))
