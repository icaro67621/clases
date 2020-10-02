import pandas as pd
import numpy as np
import random as rm

##################################
### excel con python

archivo = pd.ExcelFile('c:/Users/USER/Documents/programas/ejemplo.xlsx')
print(archivo.parse('Hoja1'))

###################################
#### leer CSV

archivo1 = pd.read_csv('c:/Users/USER/Documents/programas/poblacion.csv')
print(archivo1)
print("La Ciudad mas poblada de {} es {}".format(archivo1['Continente'][3],archivo1['Ciudad más poblada'][3]))