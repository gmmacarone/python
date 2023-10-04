"""Disponer un Listbox con una serie de nombres de frutas. Permitir la selección solo de uno de ellos. Cuando se presione un botón recuperar la fruta seleccionada y mostrarla en una Label."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Frutas")

        #listado
        self.listbox=tk.Listbox(self.window)
        self.listbox.grid(column=0,row=0)
        self.listbox.insert(0,"papa")
        self.listbox.insert(1,"lechuga")
        self.listbox.insert(2,"remolacha")

        #boton
        self.boton=tk.Button(self.window,text="Recuperar",command=self.recuperar)
        self.boton.grid(column=0,row=2)

        #mostrar
        self.label=tk.Label(self.window,text=" ")
        self.label.grid(column=0,row=3)

        self.window.mainloop()

    def recuperar(self):
        if len(self.listbox.curselection())!=0:
            self.label.configure(text=self.listbox.get(self.listbox.curselection()[0]))

#main
app=Aplicacion()