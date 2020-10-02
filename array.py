import numpy as np
hola = np.zeros(5)
hola2 = np.ones(5)
print(hola)
print(hola2)
hola3 = np.arange(10)
print(hola3)
hola4 = np.arange(5,21,2)
print(hola4)
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
arreglo1 = np.array(lista1)
print(type(arreglo1))
arreglo_doble = (lista1,lista2)
array_doble = np.array(arreglo_doble)
print(arreglo_doble)
print(array_doble)
print("Esta es una prueba")

##############################################
#############operaciones con arrays
##############################################

nuevo = np.array([1,2,3,4])
nuevo1 = nuevo + 2
sencilla = np.array(([1,2,3],[4,5,6],[7,8,9]))
print (sencilla)
copia  = sencilla.copy()
copia = copia ** 2
print(copia)
sencilla[1][1]=8
print(sencilla)

#############################################
########### matrices transpuestas
#############################################

ejercicio = np.arange(10,160,10).reshape((5,3))
print(ejercicio)
ejercicio = ejercicio.T
print(ejercicio)
###########################################
######### funciones
nueva_array = np.sqrt(np.random.rand(5))
nueva_array2 = np.sqrt(np.random.rand(5))

suma = np.add(nueva_array,nueva_array2)
print(nueva_array)
print(nueva_array2)
print(suma)