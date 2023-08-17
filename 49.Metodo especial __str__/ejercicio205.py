"""Definir una clase llamada Punto con dos atributos x e y.
Crearle el método especial __str__ para retornar un string con el formato (x,y)."""

class Punto:
    def __init__(self,x,y):
        self.__x = x #Atributo privado
        self._y= y   #Atributo protegido
    
    def __str__(self):
        return f"({self.__x},{self._y})"
#main
p1 = Punto(20,-3)
print("Punto 1:", p1)


    