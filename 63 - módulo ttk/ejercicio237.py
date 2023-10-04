"""Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados. Utilizar Widget del módulo ttk."""


import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Lenguaje")

        #selecciones
        self.seleccion1=tk.IntVar()
        self.check1=ttk.Checkbutton(self.window,text="Java",variable=self.seleccion1,command=self.cuenta)
        self.check1.grid(column=0,row=0)

        self.seleccion2=tk.IntVar()
        self.check2=ttk.Checkbutton(self.window,text="C",variable=self.seleccion2,command=self.cuenta)        
        self.check2.grid(column=0,row=1)

        self.seleccion3=tk.IntVar()
        self.check3=ttk.Checkbutton(self.window,text="Python",variable=self.seleccion3,command=self.cuenta)
        self.check3.grid(column=0,row=2)

        #mostar en label
        self.label=ttk.Label(self.window,text="Cuenta")
        self.label.grid(column=0,row=3)

        self.window.mainloop()

    def cuenta(self):
        total=0
        if self.seleccion1.get()==1:
            total+=self.seleccion1.get()
        if self.seleccion2.get()==1:
            total+=self.seleccion2.get()
        if self.seleccion3.get()==1:
            total+=self.seleccion3.get()
        self.label.configure(text=total)
#main
app=Aplicacion()