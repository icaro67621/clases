import sqlite3
##################################crear base de datos
conexion = sqlite3.connect("basededatos2.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE Productos1 (id text,nombre text,precio integer)")
lista_productos = [('1','impresora',300),('2','raton',20),('3','ordenador',600)]
cursor.executemany("INSERT INTO Productos1 VALUES (?,?,?)",lista_productos)
cursor.execute("SELECT * FROM Productos1")
lista_nueva = cursor.fetchall()

for valor in lista_nueva:
	print(valor)
conexion.commit()
conexion.close()