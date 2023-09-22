"""Disponer un control Checkbutton que muestre el siguiente mensaje: ¿Está de acuerdo con los términos y condiciones?, además agregar un Button desactivo. Cuando se tilde el Checkbutton inmediatamente activar el botón."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        # Crear la ventana principal
        self.window=tk.Tk()
        self.window.title("Contrato")

        #seleccion
        self.seleccion=tk.IntVar()
        self.check=tk.Checkbutton(self.window,text="Acepta Terminos?",variable=self.seleccion,command=self.elige)
        self.check.grid(column=0,row=0)

        #boton
        self.boton=tk.Button(self.window,text="Aceptar",state="disable")
        self.boton.grid(column=0,row=1)

        self.window.mainloop()
    def elige(self):
        if self.seleccion.get()==1:
            self.boton.configure(state="normal")
        else:
            self.boton.configure(state="disable")


        

#main
app=Aplicacion()