"""Mostrar una ventana y en su interior dos botones y una label utilizando el módulo ttk. La label muestra inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label"""

import tkinter as tk
from tkinter import ttk


class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Controles")

        self.valor=0
        self.label=ttk.Label(self.window,text=self.valor)
        self.label.grid(column=1,row=0)
        self.label.configure(background="red")

        self.botonMas=ttk.Button(self.window,text="+",command=self.incrementar)
        self.botonMas.grid(column=0,row=1)

        self.botonMenos=ttk.Button(self.window,text="-",command=self.decrementar)
        self.botonMenos.grid(column=2,row=1)

           

        self.window.mainloop()
    
    def incrementar(self):
        self.valor+=1
        self.label.configure(text=self.valor)



    def decrementar(self):
        self.valor-=1
        self.label.configure(text=self.valor)

#main
app=Aplicacion()