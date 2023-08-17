"""Veamos con un ejemplo la sintaxis para redefinir el operador +.
Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne la suma de los depósitos de los dos clientes que estamos sumando."""

class Cliente:
    def __init__(self,nombre,monto):
        self.__nombre = nombre 
        self.__monto = monto
    
    def __add__(self,objeto2):
        sum=self.__monto+objeto2.__monto
        return sum
#main
cliente1=Cliente("Ana",2000)
cliente2=Cliente("Pepe",400)
print("La suma de los montos ")
print(cliente1+cliente2)