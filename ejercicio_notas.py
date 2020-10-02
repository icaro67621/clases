print("Coloca Nota1")
nota1 = input()
nota1 = int(nota1)
print("Coloca Nota2")
nota2 = input()
nota2 = int(nota2)
print("Coloca Nota3")
nota3 = input()
nota3 = int(nota3)
promedio = nota1+nota2+nota3
promedio2 = promedio/3
print("tu promedio es {}".format(promedio2)) 
if promedio2 >= 5:
	print("Aprobado")
else:
	print("Reprobado")