"""Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias frutas. Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas en una Label.

"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title(("Frutas"))

        #listado
        self.listbox=tk.Listbox(self.window,selectmode=tk.MULTIPLE)
        self.listbox.grid(column=0,row=0)
        self.listbox.insert(0,"papa")
        self.listbox.insert(1,"lechuga")
        self.listbox.insert(2,"rucula")

        #boton
        self.boton=tk.Button(self.window,text="Recurepar",command=self.recuperar)
        self.boton.grid(column=0,row=2)

        #mostrar
        self.label=tk.Label(self.window,text=" ")
        self.label.grid(column=0,row=3)

        self.window.mainloop()


    def recuperar(self):
        if len(self.listbox.curselection())!=0:
            todas=""
            for i in self.listbox.curselection():
                todas+=self.listbox.get(i)+"\n"
            self.label.config(text=todas)


#main
app=Aplicacion()