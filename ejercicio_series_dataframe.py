import pandas as pd
import numpy as np
import random as rm

lista_clase = ["Clase1","Clase2","Clase3"]
valores_clase = [np.random.randint(1,100),np.random.randint(1,100),np.random.randint(1,100)]
serie = pd.Series(valores_clase,index=lista_clase)
print(serie)
print(serie["Clase2"])