import pandas as pd
import numpy as np
import random as rm

##################################
### html con python

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'
frame = pd.io.html.read_html(url)
frame_futbol=frame[0]
frame_futbol=frame_futbol.drop('Notas',axis=1)
print(frame_futbol)
print(frame_futbol.loc[10]['Campeón'])
#print(frame_futbol[['Campeón','10']])