import pandas as pd
import numpy as np
import random as rm

lista_1 = np.arange(3)
indices = ['i1','i2','i3']
serie = pd.Series(lista_1,index=indices)
serie = serie * 2
print(serie['i2'])
print(serie[0:3])
print(serie['i1':'i3'])
print(serie[serie>=2])

valores = np.arange(25).reshape(5,5)
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['c1','c2','c3','c4','c5']
data_fm = pd.DataFrame(valores,index=lista_indices,columns=lista_columnas)
print(data_fm)
print(data_fm['c3']['i3'])#primero va las columnas y luego las filas o indices
print(data_fm[['c2','c5']])
print(data_fm[data_fm['c2']>15])
print(data_fm.loc['i3'])
print(data_fm.loc['i3']['c4'])#primero va los indices y luego las columnas por el 

############TIP

lista_diferente = list('abcdefgh')
print(lista_diferente)

#############################################################
#### operaciones sobre series y dataframes//ordenar y clasificar series

valores_serie=range(5)
valores_index_88=list('bcadz')
new_serie=pd.Series(valores_serie,index=valores_index_88)
print(new_serie)
print(new_serie.sort_index())
print(new_serie.sort_values())
print(new_serie.rank())
serie_rank=pd.Series(np.random.randn(15))## numeros random
print(serie_rank.rank())
