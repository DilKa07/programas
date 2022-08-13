import random
lista_numeros = []

for indice in range(1,11):
	lista_numeros.append(random.randint(1,10))

for numero in lista_numeros:
	print(numero," ",numero * 2," ",numero * 3)