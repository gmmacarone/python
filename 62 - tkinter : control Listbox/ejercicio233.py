"""Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Datos")

        self.label1=tk.Label(self.window,text="Nombre")
        self.label1.grid(column=0,row=0)

        self.nombre=tk.StringVar()
        self.entry1=tk.Entry(self.window,width=10,textvariable=self.nombre)
        self.entry1.grid(column=0,row=1)

        self.boton=tk.Button(self.window,text="Eleccion",command=self.recuperar)
        self.boton.grid(column=0,row=2)


        self.scroll=tk.Scrollbar(self.window,orient=tk.VERTICAL)

        self.listbox=tk.Listbox(self.window,selectmode=tk.SINGLE,yscrollcommand=self.scroll.set)
        self.listbox.grid(column=0,row=3)
        self.scroll.grid(column=1,row=3,sticky="NS")
        self.scroll.configure(command=self.listbox.yview)
        self.listbox.insert(0,"Argentina")
        self.listbox.insert(1,"Shile")
        self.listbox.insert(3,"Peru")
        self.listbox.insert(4,"Paraguay")
        self.listbox.insert(5,"Brasil")
        self.listbox.insert(6,"Uruguay")
        self.listbox.insert(7,"Mexico")
        self.listbox.insert(8,"Colombia")
        self.listbox.insert(9,"Venezuela")
        self.listbox.insert(10,"Panama")
        self.listbox.insert(11,"EEUU")
        self.listbox.insert(12,"Canada")


        self.label2=tk.Label(self.window,text=" ")
        self.label2.grid(column=0,row=4)

        self.window.mainloop()

        
    def recuperar(self):
        

        texto=""
        if len(self.listbox.curselection())!=0 and self.nombre.get()!="":
            texto=self.nombre.get() +" "+ self.listbox.get(self.listbox.curselection()[0])
            self.label2.configure(text=texto)
        else:
            self.label2.configure(text="Complete campos")

#main
app=Aplicacion()