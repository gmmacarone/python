"""Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: 
nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del 
nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con 
mayor antigüedad en el club."""

class Club:
    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()
    
    def mayor(self):

        if self.socio1.ant>self.socio2.ant and self.socio1.ant>self.socio3.ant:
            print("MAS ANTIGUO ",self.socio1.nombre) 
        elif self.socio2.ant>self.socio1.ant and self.socio2.ant>self.socio3.ant:
            print("MAS ANTIGUO",self.socio2.nombre)
        elif self.socio3.ant>self.socio1.ant and self.socio3.ant>self.socio2.ant:
            print("MAS ANTIGUO",self.socio3.nombre)

class Socio:
    def __init__(self):
        self.nombre=input("Ingrese nombre :")
        self.ant=int(input("Ingrese antiguedad :"))
        

#main
club=Club()
club.mayor()