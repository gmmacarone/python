"""Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer", cuando se presione un botón actualizar una Label con el Radiobutton seleccionado."""


import tkinter as tk
from tkinter import ttk


class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Sexo")
        #etiqueta de sexo
        self.label=ttk.Label(self.window,text="Mostrar")
        self.label.grid(column=0,row=0)

        #seleccion
        self.seleccion=tk.IntVar()
        self.seleccion.set(0)
        self.radio1=ttk.Radiobutton(self.window,text="Hombre",variable=self.seleccion,value=1,command=self.eleccion)
        self.radio1.grid(column=0,row=1)

        self.radio2=ttk.Radiobutton(self.window,text="Mujer",variable=self.seleccion,value=2,command=self.eleccion)
        self.radio2.grid(column=0,row=2)


        self.window.mainloop()
    def eleccion(self):
        if self.seleccion.get()==1:
            self.label.configure(text="HOMBRE")
        else:
            self.label.configure(text="MUJER")

#main
app=Aplicacion()
