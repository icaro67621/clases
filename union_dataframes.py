import pandas as pd

tupla1 = {'C1':['a','b','c'],'Claves':['1','2','3']}
tupla2 = {'C2':['a','b','c'],'Claves':['3','5','1']}
frame1 = pd.DataFrame(tupla1)
print(frame1)
frame2 = pd.DataFrame(tupla2)
print(frame2)
frame3 = pd.DataFrame.merge(frame1,frame2)
print(frame3)

############## ahora le vamos a dar prioridad al dataframe1 basado en claves
frame4 = pd.DataFrame.merge(frame1,frame2,on='Claves',how='left')
print(frame4)
############## ahora le vamos a dar prioridad al dataframe2 basado en claves
frame5 = pd.DataFrame.merge(frame1,frame2,on='Claves',how='right')
print(frame5)
############## ahora vamos a hacer un merge de todo
frame6 = pd.DataFrame.merge(frame1,frame2,on='Claves',how='outer')
print(frame6)