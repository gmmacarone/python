"""Mostrar dos Label, en una se muestra el nombre del programa y en la segunda el año de creación. Disponer un botón para finalizar el programa.
No permitir al usuario redimensionar la ventana."""

import tkinter as tk
import sys

class Aplication:
    def __init__(self):
        self.window=tk.Tk()  #creo la ventana
        self.window.resizable(False,False) #la dejo no redimensionable
        
        self.nombre="Ubuntu"   #un sticker
        self.anio=2020  #otro

        #aca pongo los sticker dentro de la window y los posiciono
        
        self.label1=tk.Label(self.window,text=self.nombre)
        self.label1.grid(column=0,row=0)
        
        self.label2=tk.Label(self.window,text=self.anio)
        self.label2.grid(column=0,row=1)

        #un boton de FIN que llama a la funcion para cerrar el programa
        self.botonFin=tk.Button(self.window,text="Fin",command=self.finalizar)
        self.botonFin.grid(column=0,row=2)

        self.window.mainloop()

    #esto finaliza el app    
    def finalizar(self):
        sys.exit(0)
#main
app=Aplication()