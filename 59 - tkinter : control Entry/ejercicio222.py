"""Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Sumando")

        self.label1=tk.Label(self.window,text=" Ingrese un número : ")
        self.label1.grid(column=0,row=0)

        self.num1=tk.StringVar()
        self.entry=tk.Entry(self.window,width=10,textvariable=self.num1)
        self.entry.grid(column=2, row=0 )

        self.label2=tk.Label(self.window,text=" Ingrese un número : ")
        self.label2.grid(column=0,row=1)

        self.num2=tk.StringVar()
        self.entry=tk.Entry(self.window,width=10,textvariable=self.num2)
        self.entry.grid(column=2, row=1 )


        self.boton=tk.Button(self.window,text=" SUM ",command=self.sum)
        self.boton.grid(column=3 ,row = 4)

        self.label3=tk.Label(self.window,text=" Resultado :")
        self.label3.grid(column=0,row=4)

        self.resultado=tk.StringVar()
        self.resultado="     "
        self.label4=tk.Label(self.window, text=self.resultado)
        self.label4.grid( column=2, row=4)
        self.label4.configure(background="red")

        self.window.mainloop()

    def sum(self):
        suma=int(self.num1.get())+int(self.num2.get())
        self.label4.configure(text=suma)

#main
app=Aplicacion()

