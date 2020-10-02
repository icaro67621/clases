import clase_fichero_ejercicio 
import os
print("Nombre de archivo")
cadena = input()
cadena = cadena + ".txt"
print(cadena)
nuevo_fichero = clase_fichero_ejercicio.archivo(cadena)
nuevo_fichero.grabar()
nuevo_fichero.incluir()
valores = nuevo_fichero.leer()
