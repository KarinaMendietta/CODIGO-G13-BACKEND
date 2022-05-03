from tkinter import *
from tkinter import messagebox

def saludar():
    print("Hola mundo tk")
    messagebox.showinfo("Title","hola " + txtNombre.get())

app = Tk() #cree un objeto
app.title('Mi primera interfaz grafica') #este es un  metodo de Tk
app.geometry('235x600') #las medida de la ventana

frame = LabelFrame(app,text='Ventana') # frame divide la ventana, frame es un marco
frame.grid(row=0,column=0,columnspan=3,pady=10)
#ETIQUETA
lbNombre= Label(frame,text='Nombre : ') #reo una etiqueta un label 
lbNombre.grid(row=1,column=0) # ubicado en fila 1 de columna0

#CAJA DE TEXTO
txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1)

#BOTON
btnSaludo = Button(frame,text='saludar',command=saludar) #command la funcion cuando le de click
btnSaludo.grid(row=1,column=2)
app.mainloop()  #despliega osea muestra la interfaz grafica en un buucle(osea se va quedar ahi hasta q presione la x)

