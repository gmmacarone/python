"""Mostrar una ventana y en su interior dos botones y una label. La label muestra inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label"""

import tkinter as tk

class Aplication:
    def __init__(self):
        self.valor=1 #valor a controlar , inicia en 1
        self.window = tk.Tk() #creamos la ventana
        self.window.title("Controles Button y Label") #ittulo de la ventana
        self.label=tk.Label(self.window,text=self.valor)
        self.label.grid(column=0,row=0)
        self.label.configure(background="red")

        self.botonMas=tk.Button(self.window,text="Incrementa",command=self.incrementar)
        self.botonMas.grid(column=0,row=1)

        self.botonMenos=tk.Button(self.window,text="Decremento",command=self.decrementar)
        self.botonMenos.grid(column=2,row=1)

        self.window.mainloop()
    
    def incrementar(self):#funcion que se ejecuta cuando el boton mas es presionado
        self.valor += 1
        self.label.config(text=self.valor)
    
    def decrementar(self):
        #funcion que se ejecuta cuando el boton menos es presionado
        self.valor -=1
        self.label.config(text=self.valor)


       
#main
app=Aplication()

       