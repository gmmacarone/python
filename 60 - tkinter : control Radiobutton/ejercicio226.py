"""Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario.
Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):

            self.ventana1.configure(bg="red")"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Colores")

        #eleccion colores
        self.seleccion=tk.IntVar()
        self.seleccion.set(0)
        #red
        self.radio1=tk.Radiobutton(self.window,text="Red",variable=self.seleccion,value=1,command=self.elige)
        self.radio1.grid(column=0,row=0)
        #green
        self.radio2=tk.Radiobutton(self.window,text="Green",variable=self.seleccion,value=2,command=self.elige)
        self.radio2.grid(column=0,row=1)
        #blue
        self.radio3=tk.Radiobutton(self.window,text="Blue",variable=self.seleccion,value=3,command=self.elige)
        self.radio3.grid(column=0,row=2)
        """
        #boton
        self.boton=tk.Button(self.window,text="Calcular",command=self.elige)
        self.boton.grid(column=0,row=5)
        """

        self.window.mainloop()

    def elige(self):
        if self.seleccion.get()==1:
            self.window.configure(bg="red")
        elif self.seleccion.get()==2:
            self.window.configure(bg="green")
        elif self.seleccion.get()==3:
            self.window.configure(bg="blue")
                
#main
app=Aplicacion()