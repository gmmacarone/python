"""Desarrollar una clase que represente un Cuadrado y tenga
 los siguientes métodos: inicializar el valor del lado llegando como parámetro 
 al método __init__ (definir un atributo llamado lado), imprimir su perímetro 
 y su superficie."""


class Cuadrado():
    def __init__(self,lado):
        self.lado=lado
    
    def perimetro(self):
        perimetro=self.lado*4
        print("PERIMETRO :",perimetro)
    
    def superficie(self):
        superficie=self.lado*self.lado
        print("SUPERFICIE :",superficie)
#MAIN
cuadrado1=Cuadrado(5)
cuadrado1.perimetro()
cuadrado1.superficie()
    
    

