print("ingrese un numero")
numero = input()
variable = int(numero)
variable2 = 7
if (variable < variable2):
	print("la variable 1 con valor {} es menor que la variable 2 con valor {}".format(variable,variable2))
elif (variable > variable2):
	print("la variable 2 con valor {} es menor que la variable 1 con valor {}".format(variable2,variable))
else:
	print("Las variables son iguales")

for indice in range(0,variable):
	indice = indice + 10
	if (indice == 15):
		continue	
	elif(indice<17):
		print(indice)
	else:
		break
for item1 in range(4,9):
	for item2 in range(1,9):
		print(item1,item2) 
