import pandas as pd
import webbrowser

website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
#webbrowser.open(website)
#### leemos del cliboard
data = pd.read_clipboard()
print(data)
print(data.columns)
print(data['Año'])
print(data.loc[24])
print(data.head(3))
print(data.tail(3))

##################
### crear data farme con diccionario

usuarios = ['usuario1','usuario2','usuario3']
contrasenas = ['password','p455word','Password']
diccionario = {'Usuario':usuarios,'contrasenas':contrasenas}
conversion = pd.DataFrame(diccionario)
print(conversion)

##################
#### para ver indices

primer_valor = ['a','b','c']
segundo_valor = ['1','2','3']
serie_ejercicio = pd.Series(primer_valor, index = segundo_valor)
print (serie_ejercicio)
print(serie_ejercicio.index[0])
print(serie_ejercicio['2'])


#################################
#### varios datos

lista_indices = ['Camilo','Antonio','Maria']
lista_notas = [[5,4,3,3.8],[3.5,3.7,4,4.9],[3.2,3.7,4,3.9]]
lista_materias = ['Idiomas','religion','español','edu fisica']
serie_final = pd.DataFrame(lista_notas,index=lista_indices,columns=lista_materias)
print(serie_final)
print(serie_final.loc['Camilo'])
print(serie_final['religion'])