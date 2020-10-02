import pandas as pd
import numpy as numpy
import random as rm

print("ingrese tamaño de la contraseña")
size = int(input())
print("ingrese keyword")
keyword = input ()
lista = [keyword]
palabra = 'a'
print("Cuantas palabras quiere en el diccionario")
size2 = int(input())
for num0 in range(1,size2):
	for num in range(0,size):
		letra_aleatoria = rm.choice(keyword)
		if num == 0:
			palabra = letra_aleatoria
		else:
			palabra = palabra + letra_aleatoria		
	lista.append(palabra)
print(lista)





 



#### eliminbiacion de elementos en series y en dataframes
###########################################################

