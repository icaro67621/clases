#Json es una forma de almacenar e intercambiar datos
diccionario = {"carro":"hyundai","color":"blanco","costo":25000000}
import json
valor = json.dumps(diccionario)
print(valor)
diccionario2 = json.loads(valor)
print(diccionario2["carro"])
