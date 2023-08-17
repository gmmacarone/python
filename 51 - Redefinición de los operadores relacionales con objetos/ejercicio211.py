"""Plantear una clase Rectangulo. Definir dos atributos (ladomenor y ladomayor). Redefinir el operador == de tal forma que tengan en cuenta la superficie del rectángulo. Lo mismo hacer con todos los otros operadores relacionales.

"""

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura= altura
    
    def imprimir(self):
        print("Rectangulo ")
        print("Base :",self.base)
        print("Altura :",self.altura)
    
    def superficie(self):
        sup=(self.base * self.altura)
        return sup
    
    def __eq__(self,objeto2):
        if self.superficie()==objeto2.superficie():
            return True
        else:
            return False
#main
rect1= Rectangulo(50,64)
rect2= Rectangulo(5,64)
if rect1==rect2:
    print('son iguales')
else:
    print("son distintos")