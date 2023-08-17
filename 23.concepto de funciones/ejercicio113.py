"""Confeccionar una aplicacion que solicite la carga de dos valores enteros y muestre su suma 
repetir la carga impresion de la suma cinco veces , mostrar una linea separadora 
despues que cargamos dos valores y su suma"""

def carga_suma():
    valor1=int(input("Carga el valor :"))
    valor2=int(input("Carga el otro valor :"))
    suma=valor1+valor2
    print("La suma es :",suma)

def linea():
    print("____________________________")


for i in range(5):
    carga_suma()
    linea()
    
