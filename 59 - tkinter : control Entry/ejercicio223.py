"""Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:"""


import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title(" Verificando....")

        #etiqueta Usuario
        self.label1=tk.Label(self.window,text=" Usuario : ")
        self.label1.grid(column=0,row=0)
       
        #casillero para completar
        self.usuario=tk.StringVar()
        self.entry_usuario = tk.Entry (self.window , width='10',textvariable=self.usuario)
        self.entry_usuario.grid(column=2,row=0)
        

        #etiqueta Clave
        self.label2=tk.Label(self.window,text=" Password : ")
        self.label2.grid(column=0,row=3)
        
        #casillero para completar
        self.password=tk.StringVar()
        self.entry_password = tk.Entry (self.window , width='10',show="*",textvariable=self.password)
        self.entry_password.grid(column=2,row=3)
       

        #boton
        self.button = tk.Button(self.window, text ="Ingresar", command=self.ingresar )
        self.button.grid(column=2,row=4) 

        self.window.mainloop()
        
    # funcion
    def ingresar(self):
        us=self.usuario.get()
        pas=self.password.get()
        print(us)
        print(pas)
        if (us=="juan" and pas=="abc123"):
            self.window.title(" CORRECTO ")
            print ("OK")
        else:
            print("NO")
            print(us)
            print(pas)
            print(type(self.password))
            self.window.title(" no CORRECTO ")
    
   
#main
app=Aplicacion()