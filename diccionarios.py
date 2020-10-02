primero = {"green":"verde","blue":"azul","white":"blanco"}
segundo = {"green":"verde","blue":"azul","white":"blanco"}
print(primero)
tamaño = len(primero)
print(tamaño)
color = primero["green"]
print(color)
primero["orange"] = "naranja"
print(primero)
primero.pop("blue")
print(primero)
del(primero["green"])
print(primero)
for contador,contador1 in segundo.items():
	 print(contador,contador1)
