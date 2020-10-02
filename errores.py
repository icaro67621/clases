numero = 0
numero2 = 2

try:
	numero_final = numero2/numero
except ZeroDivisionError:
	print("Fail Fail")
except: 
	print("Fail")
else:
	print("Ok")
finally:
	print("Este ejercicio se ha acabado")