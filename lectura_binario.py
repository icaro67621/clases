import pickle
colorers = ["azul","naranja","verde","majenta"]
fichero = open("colores.pckl","wb")
pickle.dump(colorers,fichero)#(la lista,el archivo)
fichero.close()
#ahora leo los datos
fichero = open("colores.pckl","rb")
print(pickle.load(fichero))
fichero.close()
#ejercicio de binarios
parejas = {"manzana":"apple","naranja":"orange","limon":"lemon"}
print(parejas.values())
fichero2 = open("ejercicio.pckl","wb")
pickle.dump(parejas,fichero2)
fichero2.close()
fichero3 = open("ejercicio.pckl","rb")
valor = pickle.load(fichero3)
print(valor)
print(valor.values())
fichero2.close()






