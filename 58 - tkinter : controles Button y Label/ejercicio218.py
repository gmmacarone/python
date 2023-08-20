"""Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer", al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado."""


import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("sexo")

        #self.label=tk.Label(self.window)
        #self.label.grid(column=0,row=0)
        #self.label.configure(background="red")
        

        self.botonHombre=tk.Button(self.window,text="Hombre",command=self.hombre)
        self.botonHombre.grid(column=0,row=1)

        self.botonMujer=tk.Button(self.window,text="Mujer",command=self.mujer)
        self.botonMujer.grid(column=0,row=2)

        self.window.mainloop()

    def hombre(self):
        self.window.title("HOMBRE")
        #self.label.config(text="HOMBRE")
    
    def mujer(self):
        self.window.title("MUJER")
        #self.label.config(text="MUJER")
#main
app=Aplicacion()