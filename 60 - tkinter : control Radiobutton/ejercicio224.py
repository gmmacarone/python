"""Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer", cuando se presione un botón actualizar una Label con el Radiobutton seleccionado."""



import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Selección")

        #eleccion
        self.seleccion=tk.IntVar()
        self.seleccion.set(0)
        self.radio1=tk.Radiobutton(self.window,text="Varón",variable=self.seleccion,value=1)
        self.radio1.grid(column=0,row=0)

        self.radio2=tk.Radiobutton(self.window,text="Mujer",variable=self.seleccion,value=2)
        self.radio2.grid(column=0,row=1)
        

        #boton
        self.button=tk.Button(self.window,text="Elejir",command=self.mostrar)
        self.button.grid(column=0,row=3)

        #donde lo muestra
        self.label1=tk.Label(self.window,text="Mostrar selección")
        self.label1.grid(column=0,row=4)

        
        self.window.mainloop()
    def mostrar(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="Varon")
        else:
            self.label1.configure(text="Mujer")
        
       
        
#main
app=Aplicacion()        