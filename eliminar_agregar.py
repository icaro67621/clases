import pandas as pd
import numpy as numpy
import random as rm

print("ingrese tamaño de la contraseña")
size = int(input())
print("ingrese keyword")
keyword = input ()
print("ingrese el año")
keyword1 = input ()
lista = [keyword]
palabra = 'a'
print("Cuantas palabras quiere en el diccionario")
size2 = int(input())
print("Ingrese el dominio")
dominio = input()
usuario = keyword + "@" + dominio + ".com" 
lista2 = [usuario]
for num0 in range(1,size2):
	for num in range(0,size):
		letra_aleatoria = rm.choice(keyword+keyword1)
		if num == 0:
			palabra = letra_aleatoria
		else:
			palabra = palabra + letra_aleatoria		
	lista.append(palabra)
	lista2.append(usuario)
diccionario = {'Usuario':lista2,'contrasenas':lista}
conversion = pd.DataFrame(diccionario)
#### eliminbiacion de elementos en series y en dataframes
###########################################################
conversion = conversion.drop(0)
print(conversion)



