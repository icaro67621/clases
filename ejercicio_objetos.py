class CARRO:
	"""docstring for CARRO"""
	def __init__(self,marca,color,combustible,cilindrada):
		self.marca = marca
		self.color = color
		self.combustible = combustible
		self.cilindrada = cilindrada
def mostrar(objeto):
	print(objeto.marca)
	print(objeto.color)
	print(objeto.combustible)
	print(objeto.cilindrada)
coche1 = CARRO("Opel","Rojo","gasolina","1500")
mostrar(coche1)
################################################################
resultado = lambda numero1,numero2,numero3 : (numero1 + numero2 + numero3)/3
total = resultado(5,10,15)
print("el resultado promedio es {}".format(total))