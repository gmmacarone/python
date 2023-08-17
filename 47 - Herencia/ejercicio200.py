"""Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado."""

class Persona():
    def __init__(self):
        self.nombre=input("Ingrese el nombre :")
        self.edad=int(input("Ingrese la edad :"))
    def imprimir(self):
        print ("Nombre: ", self.nombre)
        print ("Edad:", self.edad)
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        #super() nos permite acceder al constructor padre sin necesidad de escribir su
        #nombre explícitamente, lo que hace más fácil mantener nuest
        #código limpio e independiente de las modificaciones realizadas
        self.sueldo_base = float ( input("Ingrese sueldo :"))
    def impuesto(self):
        super().imprimir()
        if self.sueldo_base>3000:
            
            print("Impuesto aplicado , debe PAGAR")
        else:
            
            print("No paga!")
#main
persona1=Empleado()  #<-- Creando una instancia de empleado her
print("\nDatos del empleado:")
#persona1.imprimir()
persona1.impuesto()