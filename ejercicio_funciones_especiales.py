

def primos(numero1):
	conteo = 0
	for num in range(1,numero1):
		for num2 in range(1,numero1):
			#print(" {} / {}".format(num,num2))
			valor = num % num2 
			#print(" = {}".format(valor))
			if valor == 0:
				conteo = conteo + 1
				#print("El conteo va en {}".format(conteo))
		if conteo == 2:
			#print("Primo = {}".format(num))
			yield num
		conteo = 0
maxi = 100
numeral = list(primos(maxi))
#division = 3%3
#print("el valor es {}".format(division))
#for new in numeral:
print(numeral)

def mayor(entero):
	if (entero <= 50):
		return (True)
	else:
		return (False)	

filtro = filter(mayor,numeral)

lista = list(filtro)
print(lista)
