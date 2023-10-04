"""Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto". Utilizar Widget del módulo ttk."""


import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Acceso")
        #etiqueta de usuario
        self.label1=ttk.Label(self.window,text="Usuario")
        self.label1.grid(column=0,row=0)
        #entrada de usuario
        self.usuario=tk.StringVar()
        self.entrada_us=ttk.Entry(self.window,width=10,textvariable=self.usuario)
        self.entrada_us.grid(column=0,row=1)

        #etiqueta contraseña
        self.label2=ttk.Label(self.window,text="Clave")
        self.label2.grid(column=0,row=2)
        #entrada de contraseña
        self.contrasena=tk.StringVar()
        self.entrada_clave=ttk.Entry(self.window,width=10,textvariable=self.contrasena)
        self.entrada_clave.grid(column=0,row=3)


        #boton
        self.boton=ttk.Button(self.window,text="Click",command=self.validar)
        self.boton.grid(column=0,row=4)



       
        self.window.mainloop()

    def validar(self):
        if self.contrasena.get()=="abc123" and self.usuario.get()=="juan":
            self.window.title("Accediendo...")
        else:
            self.window.title("ERROR")

#main
app=Aplicacion()