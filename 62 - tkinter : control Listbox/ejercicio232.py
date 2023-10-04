"""
Por defecto no aparece una barra de scroll si la cantidad de item supera el tamaño del cuadro del Listbox. Para que se muestre una barra de scroll la debemos crear y enlazar con el Listbox.
El mismo programa anterior pero con la barra de scroll queda:

Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias frutas. Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas en una Label.

"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Scroll")
        #scroll
        self.scroll=tk.Scrollbar(self.window,orient=tk.VERTICAL)
                
        #listdo
        self.listbox=tk.Listbox(self.window,selectmode=tk.MULTIPLE,yscrollcommand=self.scroll.set)
        self.listbox.grid(column=0,row=0)
        self.scroll.grid(column=1,row=0,sticky="NS")
        self.scroll.configure(command=self.listbox.yview)
        self.listbox.insert(0,"papa")
        self.listbox.insert(1,"lechuga")
        self.listbox.insert(3,"peras")
        self.listbox.insert(4,"pimientos")
        self.listbox.insert(5,"melon")
        self.listbox.insert(6,"limon")
        self.listbox.insert(7,"kiwi")
        self.listbox.insert(8,"banana")
        self.listbox.insert(9,"uva")
        self.listbox.insert(10,"papaya")
        self.listbox.insert(11,"mandarina")
        self.listbox.insert(12,"frutilla")
        

        #boton
        self.button=tk.Button(text="Aceptar",command=self.recuperar)
        self.button.grid(column=0,row=2)

        #mostrar
        self.label=tk.Label(self.window,text="--------")
        self.label.grid(column=0,row=3)
        
        self.window.mainloop()
    def recuperar(self):
        todas=""
        for i in self.listbox.curselection():
            todas+=self.listbox.get(i)+"\n"
        self.label.config(text=todas)

#main
app=Aplicacion()
