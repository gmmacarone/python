"""Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Lenguajes")

        #grupo de selecciones
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.window,text="Python",variable=self.seleccion1,command=self.cuenta)
        self.check1.grid(column=0,row=0)

        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.window,text="Java",variable=self.seleccion2,command=self.cuenta)
        self.check2.grid(column=0,row=1)

        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.window,text="C++",variable=self.seleccion3,command=self.cuenta)
        self.check3.grid(column=0,row=2)

        #donde lo muestra
        self.resultado=tk.StringVar()
        self.label1=tk.Label(text="Cantidad")
        self.label1.grid(column=0,row=3)

        self.label2=tk.Label(self.window,text=self.resultado)
        self.label2.grid(column=0,row=4)



        self.window.mainloop()

    def cuenta(self):
        add=0
        if self.seleccion1.get()==1:
            add+=1
        if self.seleccion2.get()==1:
            add+=1
        if self.seleccion3.get()==1:
            add+=1
        self.label2.configure(text=add)
#main
app=Aplicacion()