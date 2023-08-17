"""Crear un diccionario que permita almacenar 5 artículos, 
utilizar como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100."""


def cargar():
    productos={}
    for i in range(3):
        nombre=input("Ingrese el nombre :")
        precio=int(input("Ingrese el precio :"))
        productos[nombre]=precio
    return productos

def imprimir(productos):
    for item in productos:
        print(item,productos[item])

def mayor(productos):
    for item in productos:
        if productos[item]>100:
            print(".........................")
            print("Productos mayor a $100")
            print(item,productos[item])


#main
#productos={"Yerba":800,"Azucar":340,"Arroz":200,"Te":50}
productos=cargar()
imprimir(productos)
mayor(productos)