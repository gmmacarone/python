"""Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo."""

class Triangulo():

    def inizializar(self,lado1,lado2,lado3):
        self.a = lado1 #atributo de instancia a del objeto triang
        self.b = lado2
        self.c = lado3
    def mayor(self):
        if self.b<self.a>self.b:
            return (F"El {self.a} es el mayor")
        elif  self.a < self.b > self.c :
            return (f"El {self.b} es el mayor")
        elif self.a < self.c > self.b :
            return (f"El {self.c} es el mayor")
    def equilatero(self):
        if self.a == self.b and self.b==self.c:
            print("Es un Equilátero.")
    
#main
triangulo1=Triangulo()
triangulo1.inizializar(3,5,7)
print(triangulo1.mayor())
triangulo1.equilatero()
print("___________")
triangulo1.inizializar(3,3,3)
print(triangulo1.mayor())
triangulo1.equilatero()