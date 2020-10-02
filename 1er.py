print("ingrese un numero")
numero = input()
numero = int(numero)
if numero < 0 and numero != 10:
    numero = 0
    print("El número ingresado es negativo cambiado a cero.\n")
#elif numero == 0:
#    print("El número ingresado es 0.\n")
#elif numero == 1:
#    print("El número ingresado es 1.\n")
#else:
#    print("El número ingresado es mayor que uno.\n")