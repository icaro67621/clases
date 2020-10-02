primero = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}
print(primero["naranja"])
primero["Piña"]="pineapple"
variable = int(len(primero))
for inicial,inicial2 in primero.items():
	print("la palabra {} en ingles es {}".format(inicial,inicial2))

#####################################################################################
# este es el programa de las notas del ejercicio de bucles
nota=3.5
trabajo_realizado="si"
if (nota >= 4) and (trabajo_realizado == "si"):
	nota_final = "Aprobado"
	print("Tu trabajo final esta en :"+nota_final)
else:
	nota_final = "Suspenso"
	print("Tu trabajo final esta en :"+nota_final)