"""Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club."""

class Socio():
    def __init__(self):
        self.nombre = input("Ingrese el nombre del socio:")
        self.ant=int(input("Ingrese antigüedad :"))
    def antiguedad(self):
        return self.ant
    def imprimir(self):
        return ("Nombre:",self.nombre,"Antigüedad",self.ant)
    
class Club():
    def __init__(self):
        #Cargando datos de socios
        print("\t\tDatos de los socios:")
        self.socio1=Socio()
        #self.socio1.imprimir()
        self.socio2=Socio()
        #self.socio2.imprimir()
        self.socio3=Socio()
        #self.socio3.imprimir()

    def mayor_ant(self):
        print("El socio mas antigüo es ")
        if (self.socio1.antiguedad()>self.socio2.antiguedad() and self.socio1.antiguedad()>self.socio3.antiguedad()):
            print(self.socio1.imprimir())
        elif (self.socio2.antiguedad()>self.socio1.antiguedad()) and (self.socio2.antiguedad()>self.socio3.antiguedad()):
            print(self.socio2.imprimir())
        elif (self.socio3.antiguedad()>self.socio1.antiguedad() and self.socio3.antiguedad()>self.socio2.antiguedad()):
            print(self.socio3.imprimir())
        else:
            print("No hay un socio que tenga más antigüedad")
#main
c=Club()
c.mayor_ant()