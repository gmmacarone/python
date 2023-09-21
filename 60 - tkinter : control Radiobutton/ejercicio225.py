"""Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles Radiobutton permitir seleccionar si queremos sumarlos o restarlos. Al presionar un botón mostrar el resultado de la operación seleccionada."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Opere")

        #primer etiqueta
        self.label1=tk.Label(self.window,text="Primer valor")
        self.label1.grid(column=0,row=0)
        #primer entrada
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.window,width=10,textvariable=self.dato1)
        self.entry1.grid(column=0,row=1)

        #segunda etiqueta
        self.label2=tk.Label(self.window,text="Segundo valor")
        self.label2.grid(column=0,row=2)
        #segunda entrada
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.window,width=10,textvariable=self.dato2)
        self.entry2.grid(column=0,row=3)

        #boton
        self.boton=tk.Button(self.window,text="Calcular",command=self.calcula)
        self.boton.grid(column=0,row=4)

        #resultado
        self.resultado=tk.StringVar()
        self.resultado="   "
        self.label3=tk.Label(self.window,text=self.resultado)
        self.label3.grid(column=0,row=5)
        self.label3.configure(background="green")

        #eleccion
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.radio1=tk.Radiobutton(self.window,text="Suma",variable=self.seleccion,value=1)
        self.radio1.grid(column=0,row=6)

        self.radio2=tk.Radiobutton(self.window,text="Resta",variable=self.seleccion,value=2)
        self.radio2.grid(column=0,row=7)






        self.window.mainloop()
    
    
    def calcula(self):
       if self.seleccion.get()==1:
           suma=int(self.dato1.get())+int(self.dato2.get())
           self.label3.configure(text=suma)
       else:
           resta=int(self.dato1.get())-int(self.dato2.get())
           self.label3.configure(text=resta)
               

#main
app=Aplicacion()