"""Confeccionar una clase que represente un empleado. 
Definir como atributos su nombre y su sueldo. En el método __init__ cargar
 los atributos por teclado y luego en otro método imprimir sus datos y por último 
 uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)"""

class Empleado():

    def __init__(self):
        self.nombre=input("Ingrese le nombre :")
        self.sueldo=int(input("Ingrese el sueldo :$"))

    def imprimir(self):
        print("DATOS")
        print("Su nombre es :",self.nombre)
        print("Su sueldo es :$",self.sueldo)

    def impuesto(self):
        print("CALCULO IMPOSITIVO")
        if self.sueldo>3000:
            print("Debe pagar impuestos!")
        else:
            print("NO PAGA impuestos")
#main
empleado1=Empleado()
empleado1.imprimir()
empleado1.impuesto()