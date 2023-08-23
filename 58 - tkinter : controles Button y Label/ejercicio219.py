"""Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento."""


import tkinter as tk

class Aplication:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NUMEROS")

        self.valor=""
        self.label=tk.Label(self.window,text=self.valor)
        self.label.grid(column=0,row=0)
        self.label.configure(background="red")


        self.boton1=tk.Button(self.window,text="1",command=self.muestra1)
        self.boton1.grid(column=0,row=1)

        self.boton2=tk.Button(self.window,text="2",command=self.muestra2)
        self.boton2.grid(column=1,row=1)

        self.boton3=tk.Button(self.window,text="3",command=self.muestra3)
        self.boton3.grid(column=2,row=1)

        self.boton4=tk.Button(self.window,text="4",command=self.muestra4)
        self.boton4.grid(column=3,row=1)

        self.boton5=tk.Button(self.window,text="5",command=self.muestra5)
        self.boton5.grid(column=4,row=1)





        self.window.mainloop()

    def muestra1(self):
        self.valor += "1"
        self.label.configure(text=self.valor)

    def muestra2(self):
        self.valor += "2"
        self.label.configure(text=self.valor)

    def muestra3(self):
        self.valor += "3"
        self.label.configure(text=self.valor)

    def muestra4(self):
        self.valor += "4"
        self.label.configure(text=self.valor)

    def muestra5(self):
        self.valor += "5"
        self.label.configure(text=self.valor)
#main
app=Aplication()