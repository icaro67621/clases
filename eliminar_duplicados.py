import pandas as pd
import numpy as np
import random as rm

lista_valores = [[1,2],[1,2],[5,6],[5,8]]
lista_indices = list('list')
lista_columna = ['valor1','valor2']
print(lista_valores)
print(lista_indices)
print(lista_columna)
dataframe1 = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columna)
print(dataframe1)
print(dataframe1.drop_duplicates())
dataframe2 = dataframe1.drop_duplicates()
print(dataframe2.drop_duplicates(['valor1']))
print(dataframe2.drop_duplicates(['valor1'],keep='last'))

#############################
### reemplazar datos en series
serie = pd.Series([1,2,3,4,5,6],list('camilo'))
print(serie)
serie=serie.replace(1,9)
print(serie)
serie=serie.replace({2:8,3:7,4:6,5:25,6:4})
print(serie)

#########################
### renombrar indices en Dataframe 

print(dataframe1)
nuevos_indices = dataframe1.index.map(str.upper)
dataframe1.index = nuevos_indices
print(dataframe1)
dataframe1 = dataframe1.rename (index=str.lower)
print(dataframe1)
nuevos_indices2 ={'l':'c','i':'a','s':'m','t':'i'}
dataframe1 = dataframe1.rename (index=nuevos_indices2)
print(dataframe1)