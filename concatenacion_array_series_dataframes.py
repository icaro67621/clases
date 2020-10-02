import pandas as pd
import numpy as np
import random as rm

nueva = range(16)
nueva_lista = list(nueva)

for new in nueva:
	nueva_lista[new]=rm.randrange(10)

print(nueva_lista)
arreglo1 = np.array(nueva_lista)
arreglo1=arreglo1.reshape(4,4)
print(arreglo1)
for new2 in nueva:
	nueva_lista[new2]=rm.randrange(10)

print(nueva_lista)
arreglo2 = np.array(nueva_lista)
arreglo2=arreglo2.reshape(4,4)
print(arreglo2)
valor = np.concatenate([arreglo1,arreglo2])
print(valor)
itera = list(range(16))
serie1 = pd.Series(nueva_lista,index=itera)
print(serie1)
serie2 = pd.Series(nueva_lista,index=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o'])
print(serie2)
valor2 = pd.concat([serie1,serie2],keys=['serie1','serie2'])
print(valor2)


dataframe1=pd.DataFrame(np.random.rand(3,3),columns=['A','B','C'])
dataframe2=pd.DataFrame(np.random.rand(7,3),columns=['A','B','C'])
concatenado = pd.concat([dataframe1,dataframe2],keys=['dataframe1','dataframe2'])
print(concatenado)