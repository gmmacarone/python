"""Todos los ejemplos que haremos de ahora en más independientemente de su complejidad utilizaremos la metodología de POO (Programación Orientada a Objetos)

El programa anterior modificado con POO queda:

"""
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("HOLA MUNDO")
        self.ventana.mainloop()
#main
app = Aplicacion()
