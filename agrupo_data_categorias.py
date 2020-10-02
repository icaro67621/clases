import pandas as pd
import numpy as np
import random as rm

precios = [42,55,48,23,5,21,88,34,26]
rango = [0,10,20,30,40,50,60,70,80,90,100]
precios_con_rango=pd.cut(precios,rango)
print(precios_con_rango)
contador = pd.value_counts(precios_con_rango)
print(contador)


################################
##### filtrar datos en dataframe

lista_valores = np.random.rand(5,3)
print(lista_valores)
dataframe = pd.DataFrame(lista_valores)
print(lista_valores)
columna = dataframe[0]
print(columna>0,40)

#############################
##### combinaciones de elemntos dataframe

lista_valores2 = np.random.rand(5,5)
dataframe2 = pd.DataFrame(lista_valores2)
combinacion_aleatoria = np.random.permutation(5)
print(dataframe2)
print(combinacion_aleatoria)
print(dataframe2.take(combinacion_aleatoria))### reordena las filas

############################
### agrupacion de dataframe

lista_de_valores = {'clave1':['x','x','y','y','z'],'clave2':['a','b','a','b','a'],'datos1':np.random.rand(5),'datos2':np.random.rand(5)}
dataframe_group = pd.DataFrame(lista_de_valores)
print(dataframe_group)
dataagrupada = dataframe_group['datos1'].groupby(dataframe_group['clave1'])
print("La media es "+str(dataagrupada.mean()))


##################################
#### agregacion

agregacion = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]
columnas = list('abd')
dataframe_agregacion = pd.DataFrame(agregacion,columns=columnas)
print(dataframe_agregacion.agg(['sum','min']))
print(dataframe_agregacion.agg('sum',axis=1))


