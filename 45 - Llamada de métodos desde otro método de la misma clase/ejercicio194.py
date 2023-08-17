"""Plantear una clase Operaciones que solicite en el método __init__ 
la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación 
y división. Hacer cada operación en
 otro método de la clase Operación y llamarlos desde el mismo método __init__"""


class Operaciones():
    def __init__(self):
        self.num_a=int(input("Ingrese primer numero :"))
        self.num_b=int(input("Ingrese segundo numero :"))
        self.sumar()
        self.restar()

    def sumar(self):
        print("La SUMA ",self.num_a+self.num_b)
    
    def restar(self):
        print("La RESTA ",self.num_a-self.num_b)
#main
operar=Operaciones()