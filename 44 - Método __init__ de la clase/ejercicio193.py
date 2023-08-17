"""Implementar la clase Operaciones. Se deben cargar dos valores enteros 
por teclado en el método __init__, calcular su suma, resta, multiplicación 
y división, cada una en un método, imprimir dichos resultados."""

class Operaciones():

    def __init__(self,num_a,num_b):
        self.num_a=num_a
        self.num_b=num_b
    
    def suma(self):
        sum=self.num_a+self.num_b
        print(self.num_a,"+",self.num_b," = ",sum)
    def resta(self):
        res=self.num_a-self.num_b
        print(self.num_a,"-",self.num_b," = ",res)
    def multiplicacion(self):
        mul=self.num_a*self.num_b
        print(self.num_a,"x",self.num_b," = ",mul)
    def division(self):
        div=self.num_a/self.num_b
        print(self.num_a,"/",self.num_b," = ",div)
#main
operacion=Operaciones(2,5)
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()    

    