"""Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo."""

class Cuenta():
    def __init__(self):
        self.nombre_titular=None
        self.saldo = 0
        print("Bienvenido a nuestro Banco!!")
    
    def carga(self):
        self.nombre_titular=input("Defina nombre del titular :")
        self.saldo=float(input("Cuanto dinero ingresa a la cuenta :$"))
    
    def mostrar(self):
        print("\nDatos de la cuenta:")
        print("- Nombre Titular:",self.nombre_titular)
        print("- Saldo: $",format(self.saldo,'.2f'))
    
class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
    
    def interes(self):
        super().carga()
        self.saldo=self.saldo*(1.75)
        print("Plazo fijo")
        super().mostrar()

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()
    
    def caja(self):
        super().carga()
        print("Caja de Ahorro")
        super().mostrar()

#main
caja=PlazoFijo()
caja.interes()
cuenta=CajaAhorro()
cuenta.caja()
