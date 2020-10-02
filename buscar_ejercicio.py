import re
def encontrar(palabra,frase):
	variable = re.search(palabra,frase)
	return(variable)