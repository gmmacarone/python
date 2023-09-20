"""Confeccionar un programa que permita ingresar el nombre de usuario en un control Entry y cuando se presione un botón mostrar el valor ingresado en la barra de títulos de la ventana."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Aca va el nombre")

        self.label=tk.Label(self.window,text="Ingrese un nombre : ")
        self.label.grid(column=0,row=0)

        self.dato=tk.StringVar()
        self.entry=tk.Entry(self.window,width=10,textvariable=self.dato)
        self.entry.grid(column=1, row=0)

        self.boton=tk.Button(self.window,text="VIEW",command=self.view)
        self.boton.grid(column=0,row=3)

        self.window.mainloop()

    def view(self):
        nombre=str(self.dato.get())
        self.window.title(nombre)
#main
app=Aplicacion()