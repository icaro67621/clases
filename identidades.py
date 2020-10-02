#identidades
frutas = ["manzana","peras","albondoque"]
print(frutas)
frutas2 = frutas
frutas3 = ["manzana","peras","albondoque"]
frutas2.append("mentas")
print(frutas)
print(frutas2 is not frutas)
if frutas2 == frutas:
	print("pruebas exitosas")
if frutas is frutas2:
	print("mas pruebas exitosas")
#pertenencia
fruta = "manzana"
imprimir = fruta in frutas3
print(imprimir)
fruty = "manzanas"
imprimir2 = fruty in frutas3
print(imprimir2)