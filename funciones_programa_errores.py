def operacion(numero1,numero2,numero3):
	try:
		resultado1 = numero1 / (numero2-numero3)
		print("operacion correcta")
	except:
		print("operacion incorrecta")
	finally:
		print("operacion funalizada")

