"""Desarrollar una clase llamada Lista, que permita pasar al método __init__ una lista de valores enteros.
Redefinir los operadores +,-,* y // con respecto a un valor entero.

"""

class Lista:
    def __init__(self,lista):
        self.lista=lista
    
    def imprimir(self):
        print("Lista: ",self.lista)
    
    #re defino suma
    def __add__(self,numero):
        nueva_lista=[]
        for i in range (len(self.lista)):
            nuevo=(self.lista[i]+numero)
            nueva_lista.append(nuevo)
        return nueva_lista
    
    #re defino resto
    def __sub__(self,lista):
        nueva_lista=[]
        for i in range(len(self.lista)):
            nuevo=(self.lista[i]-numero)
            nueva_lista.append(nuevo)
        return nueva_lista
    
    #re defino multiplicacion
    def __mul__(self,numero):
        nueva_lista=[]
        for i in range (len(self.lista)):
            nuevo=(self.lista[i]*numero)
            nueva_lista.append(nuevo)
        return nueva_lista  

    #re defino division enteros
    def __floordiv__(self,numero):
        nueva_lista=[]
        for i in range (len(self.lista)):
            nuevo=(self.lista[i]//numero)
            nueva_lista.append(nuevo)
        return nueva_lista
        
    
#main
lista=[0,3,5,7]
lista1=Lista(lista)
numero=2
print("El numero a operar :",numero)
lista1.imprimir()
print("SUMA")
print(lista1+numero)
print("PRODUCTO")
print(lista1*numero)
print("RESTA")
print(lista1-numero)
print("DIVISION")
print(lista1//numero)