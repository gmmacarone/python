"""Desarrollar un programa que cargue los lados de un triángulo e implemente los 
siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y 
otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo."""

class Triangulo():
    def inicializar(self):
        self.lado1=int(input("Cargue un lado :"))
        self.lado2=int(input("Cargue un lado :"))
        self.lado3=int(input("Cargue un lado :"))
    
    def lado_mayor(self):
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1," ES EL MAYOR!")
        else:
            if self.lado2>self.lado3:
                print(self.lado2," ES EL MAYOR!")
            else:
                print(self.lado3," ES EL MAYOR!")
    
    def equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print(" ES EQUILATERO!")
#MAIN
triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.lado_mayor()
triangulo1.equilatero()



