import numpy as np
def pares (numero1,numero2):
	nueva = range(numero1,numero2,1)
	conteo = 0
	for new in nueva:
		if(new % 2 == 0):
			yield new
			conteo = conteo + 1

numero1=2
numero2=40
lista = list(pares(numero1,numero2))
array = np.array(lista)
print(array)
