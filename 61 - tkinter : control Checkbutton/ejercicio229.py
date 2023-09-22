"""Disponer varios objetos de la clase Checkbutton con nombres de navegadores web. En el título de la ventana mostrar todos los nombres de navegadores seleccionados.
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        #Crear la ventana
        self.window=tk.Tk()
        self.window.title("Navegadores")

        #seleccion
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.window,text="Modzilla",variable=self.seleccion1,command=self.elige)
        self.check1.grid(column=0,row=0)

        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.window,variable=self.seleccion2,text="Chrome",command=self.elige)
        self.check2.grid(column=0,row=1)

        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.window,variable=self.seleccion3,text="Opera",command=self.elige)
        self.check3.grid(column=0,row=2)

        self.window.mainloop()

    def elige(self):
        cadena=" "
        if self.seleccion1.get()==1:
            cadena+="Modzilla"
        if self.seleccion2.get()==1:
            cadena+="Chrome"
        if self.seleccion3.get()==1:
            cadena+="Opera"
        self.window.title(cadena)

#main
app=Aplicacion()

