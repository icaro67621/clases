numero = 5
numero1 = 7
numero2 = 3.7
suma = numero + numero1
print(suma)
print(numero2+numero1)
cadena = "Hola"
cadena2 = "Mundo"
concatenado = cadena + cadena2
print(concatenado)
tipo1 = type(suma)
tipo2 = type(concatenado) 
tipo3= type(numero2)
print(tipo1)
print(tipo2)
print(tipo3)
#cambio de tipo de dato 
print(type(str(numero2)))
print(cadena[3])
cadena3 = " "
cadena4=cadena+cadena3+cadena2
print(cadena4[1:])
valor = len(cadena4)
print(valor)
cadena4 = cadena4.upper()
print(cadena4)
cadena5=cadena4.split(' ')
print(cadena5)
print("No quiero que me digas (" + cadena +")")
print("Quisiera decir {} a todo el {}".format(cadena,cadena2))
print("ingrese nombre ")
variable = input()
print("welcome " + variable)