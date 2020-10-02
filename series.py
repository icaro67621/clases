import pandas as pd

serie1 = pd.Series([3,5,7])
print(serie1)
asignaturas = ['Ingles','Matematicas','Religion','Español']
notas = [4,3.5,4,2.8]
serie_notas_camilo = pd.Series(notas,index=asignaturas)
serie_notas_camilo.name = 'Notas de Camilo'
serie_notas_camilo.index.name = 'Asignaturas'
print(serie_notas_camilo)
print("La nota de Matematicas es {}".format(serie_notas_camilo['Matematicas']))
print("La materia que se perdio con menos de 3,0 fue: \n {}".format(serie_notas_camilo[serie_notas_camilo<3.0]))
###################
### puedo convertir una serie en un diccionario
diccionario_new = serie_notas_camilo.to_dict()
print(diccionario_new)

####################
# operaciones con series
notas_ana = [4.5,3.8,4,3]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)
serie_notas_ana.name = 'Notas de Ana'
serie_notas_ana.index.name = 'Asignaturas'

promedio = (serie_notas_ana + serie_notas_camilo)/2
print ("El promedio de las notas de Ana y Camilo fue \n {}".format(promedio))