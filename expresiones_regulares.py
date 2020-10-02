# esta es una prueba de encontrar una palabra en una cadena
import re
cadena = "Esta es una puta cadena"
variable = re.search("puta",cadena)
if (variable):
	print("Se encontra la cadena")
	print(variable)
	#print(span)
else:
	print("no se encontro")
#comparaciones de inicio de cadena
variable1 = re.search("^Esta",cadena)
if (variable):
	print("Se encontra la cadena")
else:
	print("no se encontro")
#comparaciones de fin de cadena
variable2 = re.search("cadena$",cadena)
if (variable2):
	print("Se encontra la cadena")
else:
	print("no se encontro")
#comparaciones de dos palabras
variable3 = re.search("es.*uni",cadena)
if (variable3):
	print("Se encontra la cadena")
else:
	print("no se encontro")
#findall
texto_nuevo = """
esta es una hermosa prueba
esta es una prueba dificil
esta es una prueba masiva
"""
print(re.findall("esta .*prueba",texto_nuevo))
#split, divide una cadena a partir de un patron
print(re.split("\s",cadena))
print(re.sub("\s","SPACE",cadena))