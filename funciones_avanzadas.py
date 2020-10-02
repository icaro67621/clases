#funiones generadoras de numeros
numero =range(0,11)
for num in numero:
	print(num)

def pares(maximo):
	for max in range(maximo):
		if ((max % 2) == 0):
			yield max
maxi = 30
numeral = pares(maxi)
for new in numeral:
	
	print(new)


#################################################

# Funcion para filtrar resultados segun uan condición
def positivo(entero):
	if (entero >= 0):
		return (True)
	else:
		return (False)	

numm = [1,-2,-4,7,8,0,3,-2]

filtro = filter(positivo,numm)

lista = list(filtro)
print(lista)

##########################################################

# aplicar una funcion a una lista
def multiplicar(multiplicador):
	return(multiplicador*2)

resultado = list(map(multiplicar,numm))
print (resultado)

###########################################################