"""Confeccionar una aplicación que permita ingresar un entero por teclado y al presionar un botón muestre dicho valor elevado al cuadrado en una Label."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Calculo de cuadrados")

        self.label1=tk.Label(self.window,text="Ingrese el número")
        self.label1.grid(column=0,row=0)

        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.window, width=10, textvariable=self.dato)
        self.entry1.grid(column=0, row=1)
        

        
        self.label2=tk.Label(self.window,text="Resultado")
        self.label2.grid(column=0,row=4)

        self.resultado=tk.StringVar()
        self.resultado="  "
        self.label1a=tk.Label(self.window,text=self.resultado)
        self.label1a.grid(column=0,row=5)
        self.label1a.configure(background="green")

        self.boton=tk.Button(self.window,text="Calcular",command=self.cuadrado)
        self.boton.grid(column=0,row=2)
        
        self.window.mainloop()
    
    def cuadrado(self):
        valor=int(self.dato.get())
        cuadrado=valor*valor
        self.label1a.configure(text=cuadrado)
        

#main
app = Aplicacion()