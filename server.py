
from http.server import BaseHTTPRequestHandler, HTTPServer #crear un servidor HTTP
import logging #escribir en consola
from datetime import date #uso de formato de fecha
import os #validación de archivo existente
import json #uso de libfreria de lectura

class S(BaseHTTPRequestHandler):#clase principal con lo q va a recibir 

    def _set_response(self):#respuesta al usuario
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        ip = self.client_address[0]
        if os.path.exists(ip+date.today().strftime("%y_%B_%a")+'.csv'):#validar existencia
            os.remove(ip+date.today().strftime("%y_%B_%a")+'.csv')#elimina archivo
        file = open(ip+date.today().strftime("%y_%B_%a")+'.csv','x')#crea archivo
        message = json.loads(post_data)#el payload lo convierto en json 
        procesos=message['proc']
        users = message['user']
        system = message['system']
        file.write(procesos)
        file.write(users)
        file.write(system)
        file.close()
        self._set_response()#enviar el status 200 html
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):#monte el web server, controlador esta en la clase S y abra el puerto 8080 
    logging.basicConfig(level=logging.INFO)#escribir en formato INFO
    server_address = ('', port)#Aqui se coloca entre las comillas la dirección IP del servidor
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()