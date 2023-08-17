"""Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)"""

class Empleado():
    def __init__(self):
        nombre=input("Ingrese nombre :")
        self.nombre = nombre
        sueldo=int(input("Ingrese sueldo  :$"))
        self.sueldo = sueldo
    def imprimir(self):
        print ("Nombre:",self.nombre)
        print ("Sueldo: $",self.sueldo)
    def impuestos(self):
        if (self.sueldo>=3000):
            print("PAGA IMPUESTOS")
        else:
            print("NO PAGAR IMPUESTO")
#main
empleado=Empleado()
empleado.imprimir()
empleado.impuestos()