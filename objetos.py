class TUERCAS:#clase
	#propiedades
	color = "azul"
	precio = 120
objeto1 = TUERCAS()
print(objeto1.color)
print(objeto1.precio)
objeto2 = TUERCAS()
objeto2.color = "verde"
print(objeto2.color)
print(objeto2.precio)
#objeto con metodos

class PERSONAS:
	"""docstring fos PERSONAS"""
	def __init__(self, nombre, edad):#cada persona va a tener unos atributos que seran el nombre y la edad
		self.nombre = nombre # cuando creemos una instancia asignaremos estos valores (nombre y edad)
		self.edad = edad

	def saludo(self):
		print("Hola me llamo {} y tengo {}".format(self.nombre,self.edad))
def sume(valor1,valor2):
	resultado = valor1 + valor2
	return resultado	
personaje = PERSONAS("Camilo Castellanos",33)
personaje.saludo()
suma = sume(5,8)
print("la suma es {}".format(suma))

#funciones

def saludo(nombre):
	print("Esta es una prueba para "+nombre)		

saludo("Arturo")

#incluir en listas
lista = ["verde","azul","rojo"]
colorin = "morado"
def inclusion(lista1,colorin1):
	lista1.append(colorin1)
inclusion(lista,colorin)
print(lista)

