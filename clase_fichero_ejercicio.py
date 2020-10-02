import os
class archivo:
	import os
	"""docstring for CARRO"""
	def __init__(self,nombre_fichero):
		self.nombre_fichero = nombre_fichero

	def grabar(self):
		fichero = open(self.nombre_fichero,"wt")
		fichero.close()

	def leer(self):
		fichero = open(self.nombre_fichero,"rt")
		datos = fichero.read()
		fichero.close()

	def incluir(self):
    
		fichero = open(self.nombre_fichero,"at")
		print("Ingrese la linea que quiere agregar")
		cadena = input()
		fichero.write("\n"+cadena)
		fichero = open(self.nombre_fichero,"rt")
		datos = fichero.read()
		fichero.close()
		return datos


		
	
