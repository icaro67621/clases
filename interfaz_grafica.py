import tkinter
from tkinter import messagebox
from tkinter import filedialog
#esto siempre va
raiz = tkinter.Tk()
raiz.title("Hola mis amigos hermosos")
#modulo frame (colocar otros componentes dentro de el)
frame = tkinter.Frame(raiz)
frame.config(bg="grey",width=400,height=200)
frame.pack()
#label, etiquetas de texto
texto = "Que tan Marica es Diego ?"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="red",bg="white",font=("Cambria",38))
etiqueta.pack()
#crear entrada por teclado
entrada = tkinter.Entry(raiz)
entrada_teclado=entrada.config(justify="center",show="X")
entrada.pack()
#definimo la funcion accion
def accion():
	print("Hola Mundo")
#creamo el boton
boton = tkinter.Button(raiz,text="Ejecutar", command=accion)
boton.pack()

def seleccionar():
	print("Tienes toda la razon {}".format(opcion.get))

#crecion de boton radio
opcion = tkinter.IntVar()
botonradio1 = tkinter.Radiobutton(raiz, text="Mucho",value=1,command=seleccionar)
botonradio1.pack()
botonradio2 = tkinter.Radiobutton(raiz, text="Demasiado",value=2,command=seleccionar)
botonradio2.pack()
botonradio1 = tkinter.Radiobutton(raiz, text="Uff que rico",value=3,command=seleccionar)
botonradio1.pack()

#creacion de checkbox
def verifico():
	print(check1.get())

check1 = tkinter.StringVar()
boton1 = tkinter.Checkbutton(raiz,text="Dennis se come a diego ?",variable=check1,onvalue="Se lo traga",offvalue="Es el pasivo",command=verifico)
boton1.pack()

#message box
def avisar():
	tkinter.messagebox.showinfo("Titular","Es un ex mechudo maricon")
Botoncito=tkinter.Button(raiz,text="Es Dennis un travesti",command=avisar)
Botoncito.pack()
#esto siempre va

#crecaion de ventana para preguntar o confirmar
def preguntar():
	resultado = tkinter.messagebox.askquestion("Titulo de pregunta","Quieres borrar este archivo?")
	if (resultado == "yes"):
		print("Estuvo bien")
	else:
		print("Estuvo mal")
botones = tkinter.Button(raiz,text="Aviso de pregunta",command=preguntar)
botones.pack()
# Ventana de abrir fichero
def apertura():
	rutafichero = filedialog.askopenfilename(title="Abrir archivo")
	print(rutafichero)
botones2 = tkinter.Button(raiz,text="Aviso de fichero",command=apertura)
botones2.pack()
raiz.mainloop()


