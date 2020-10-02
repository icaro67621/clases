colores = ["azule","verde","negro"]
variable_print = colores[1]
print(variable_print)
variable = len(colores)
print("el tamaño de la lista es {}".format(variable))
colores.append("naranja")
variable = len(colores)
print("el tamaño de la lista es {}".format(variable))
colores2 = colores
colores2.remove("verde")
variable2 = len(colores2)
cuenta = 0
print("el tamaño de la segunda lista es {}".format(variable2))
for contador in colores2:
	cuenta = cuenta + 1
	print(contador)
	print("la cuenta es {}".format(cuenta))
#tuplas
tupla_colores = ("verde","azul","amarillo")
for contador1 in tupla_colores:
	print(contador1)
