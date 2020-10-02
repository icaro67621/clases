import pandas as pd
import numpy as np
import random as rm

lista_valores = np.random.randint(0,100,50)
print(lista_valores)
lista_valores.resize(5,10)
print(lista_valores)
dataframe = pd.DataFrame(lista_valores)
print(dataframe[dataframe>40])

lista_valores2 = np.random.randint(0,100,50)
print(lista_valores2)
lista_valores.resize(5,10)
print(lista_valores2)
dataframe2 = pd.DataFrame(lista_valores2)
print(dataframe2[dataframe2>40])
