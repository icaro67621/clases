import pandas as pd
import numpy as np
import random as rm

array = np.array([[3,4,2],[8,2,7]])
frame = pd.DataFrame(array,index=['A','B'],columns=list('123'))
print(frame)
print(frame.sum())
print(frame.sum(axis=1))
print(frame.min())
print(frame.min(axis=1))
print(frame.max())
print(frame.max(axis=1))
print(frame.idxmin())
print(frame.describe())

###########################
### valores nulos
#############################

listica= ['1','2',np.nan,'4']
serie1=pd.Series(listica,index=list('abcd'))
print(serie1)
print(serie1.isnull())
serie1=serie1.dropna()
print(serie1)
array1 = np.array([[3,4,2],[8,2,7],[np.nan,2,np.nan]])
frame1 = pd.DataFrame(array1,index=['A','B','C'],columns=list('123'))
print(frame1)
print(frame1.isnull())
frame1 = frame1.fillna(88)### cambio los null por 88
#frame1=frame1.dropna()
print(frame1)

#####################
#### niveles
reversa=frame1.stack()
print(reversa)
reversa2=reversa.unstack()
print(reversa2)
