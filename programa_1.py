import modulo_ejercicio
coche1 = modulo_ejercicio.CARRO("Hyundai","I35","Gasolina","1500")
print("El carro {} es un {} de {} con un motor {} ".format(coche1.marca,coche1.color,coche1.combustible,coche1.cilindrada))
nota = 4
nota2 = 2
nota3 = 5
variable = modulo_ejercicio.resultado(nota,nota2,nota3)
print("El resultado de las notas en promedio es {}".format(variable))