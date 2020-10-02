import os
#lectura de ficheros
fichero = open("TEST.txt","rt")
datos = fichero.read()
print(datos)
#grabar ficheros
fichero2 = open("TEST_2.txt","wt")
datos_fichero = "Esta es la informacion del fichero"
fichero2.write(datos_fichero)
fichero2.close()
#inlcuir lineas
print("Ingrese la linea que quiere agregar")
cadena = input()
fichero = open("TEST.txt","at")
fichero.write("\n")
fichero.write(cadena)
fichero.close()
#borrar ficheros
os.remove("TEST_2.txt")
