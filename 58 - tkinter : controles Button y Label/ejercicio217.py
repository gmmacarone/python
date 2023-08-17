"""Mostrar dos Label, en una se muestra el nombre del programa y en la segunda el año de creación. Disponer un botón para finalizar el programa.
No permitir al usuario redimensionar la ventana."""

import tkinter as tk
import sys

class Aplication:
    def __init__(self):
        self.window=tk.Tk()
        self.window.resizable(False,False)
        
        self.nombre="Ubuntu"
        self.anio=2020
        
        self.label1=tk.Label(self.window,text=self.nombre)
        self.label1.grid(column=0,row=0)
        
        self.label2=tk.Label(self.window,text=self.anio)
        self.label2.grid(column=0,row=1)

        self.botonFin=tk.Button(self.window,text="Fin",command=self.finalizar)
        self.botonFin.grid(column=0,row=2)

        self.window.mainloop()
    
    def finalizar(self):
        sys.exit(0)
#main
app=Aplication()