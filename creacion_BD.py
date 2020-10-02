import sqlite3
##################################crear base de datos
#conexion = sqlite3.connect("camilodb.db")#creo o me conecto a mi base de datos y me devuelve el link
#conexion.close()
#############################crear tablas
#conexion = sqlite3.connect("camilodb.db")
#cursor = conexion.cursor()#nos permite ejecutar sentencias sql
#cursor.execute("CREATE TABLE Personas (nombre text,apellido1 text,apellido2 text,edad integer)")
#conexion.commit()
#conexion.close()
##############################insertar una fila en la base de datos
#conexion = sqlite3.connect("camilodb.db")
#cursor = conexion.cursor()
#cursor.execute("INSERT INTO Personas VALUES ('Ivan Camilo','Castellanos','Romero',33)")
#conexion.commit()
#conexion.close()
##############################insertar varias lineas
#conexion = sqlite3.connect("camilodb.db")
#cursor = conexion.cursor()
#lista_personas = [('Ana Luisa','Gil','Alfonsi',33),('Dennis Fabian','Mendoza','Mendoza',28),('Diego Andres','jimenez','Gonorrea',34)]
#cursor.executemany("INSERT INTO Personas VALUES (?,?,?,?)",lista_personas)
#conexion.commit()
#conexion.close()
############################consultar la data de la tabla
#conexion = sqlite3.connect("camilodb.db")
#cursor = conexion.cursor()
#cursor.execute("SELECT * FROM Personas")
#personas = cursor.fetchall()
#for persona in personas:
#	print(persona)
#conexion.close()
#########################consultar datos con de terminada condicion
conexion = sqlite3.connect("camilodb.db")
cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM Personas WHERE edad > 30")
personas = cursor.fetchall()
for numero in personas:
#	print(numero)
	conexion.close()
####################consultar datos y ordenarlos
conexion = sqlite3.connect("camilodb.db")
cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM Personas ORDER BY edad ")
personas1 = cursor.fetchall()
for numero1 in personas1:
#	print(numero1)
	conexion.close()
##########borrar datos de nuestra tabla
conexion = sqlite3.connect("camilodb.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM Personas WHERE apellido2 = 'Mendoza' ")
conexion.commit()
conexion.close()
############ctualizar datos en nuestra tabla
conexion = sqlite3.connect("camilodb.db")
cursor = conexion.cursor()
cursor.execute("UPDATE Personas set edad = 33 WHERE apellido2 = 'Alfonsi' ")
conexion.commit()
conexion.close()
