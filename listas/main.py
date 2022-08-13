milista = ["camisa", "pantalon", "falda", "blusa"]
milistanumerica = [1, 2, 3, 4, 5]
milistaalfanumerica = ["camisas", 1, "pantalones", 2]
print(milista)
print(milistanumerica)
# mostrar una cosa de la lista
print(milista[1])
print(milistaalfanumerica)
# reemplazar valor en una lista
milista[0] = "chompa"
print(milista)
# reemplazar un rango de valores en una lista
milista[1:3] = ["sombrero", "chalina"]
print(milista)
# agregar elementos a una lista
# se agrega al final
milista.append("medias")
print(milista)
# agrgar elemostos a una lista controlando el orden
milista.insert(0, "cubrecama")
print(milista)
# pasar valores de una lista a otra
# unir valores de una lista a otra
milista.extend(milistanumerica)
print(milista)
# eliminar un valor de la lista
milista.remove("chompa")
print(milista)
# eliminar un valor de la lista usando un indice
milista.pop(1)
print(milista)
# limpiar completamente la lista
# milista.clear()
# print(milista)

# imprimir mi lista uno por uno
for x in milista:
    print(x)
# agregar un elemento a mi lista
iten = input("Ingrese una prenda de ropa: ")
milista.append(iten)
print(milista)