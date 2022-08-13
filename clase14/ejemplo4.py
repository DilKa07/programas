def carga_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingresar el valor: "))
        li.append(valor)
    return li

def imprimir_mayor10(li):
    print("Elementos de la listamayores a 10: ")
    for x in range(len(li)):
        if li[x] > 10:
            print(li[x])

# BLOQUE PRINCIPAL DEL PROGRAMA

lista = carga_lista()
imprimir_mayor10(lista)