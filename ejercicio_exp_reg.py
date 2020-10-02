import buscar_ejercicio
cadena1 = "esta es una frase de pruebas para frase busquedas"
palabra = "frase"
valor = buscar_ejercicio.encontrar(palabra,cadena1)
print("La palabra inicia en la posicion {} y finaliza en la posicion {}".format(valor.start(),valor.end()))
