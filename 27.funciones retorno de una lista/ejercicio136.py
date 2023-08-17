"""Desarrollar una aplicación que permita ingresar por teclado los nombres de 
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos 
con un precio menor igual al valor ingresado."""


def carga():
    nombre=[]
    precio=[]
    for i in range (5):
        nom=input("Nombre del articulo :")
        pre=int(input("Ingrese el precio :$"))
        nombre.append(nom)
        precio.append(pre)
    return[nombre,precio]

def imprimir(nombre,precio):
    for i in range (5):
        print(nombre[i],"vale :$",precio[i])
        print("***************")

def mayor(nombre,precio):
    aux=precio[0]
    indice=0
    for i in range(5):
        if precio[i]>aux:
            aux=precio[i]
            indice=i
    print("El articulo de mayor precio :",nombre[indice],"$",aux)

def menor_teclado(valor,nombre,precio):
    for i in range(5):
        if precio[i]<=valor:
            print("Producto :",nombre[i],"$",precio[i],"menor a :$",valor)
#main

#1) Cargar los nombres de articulos y sus precios.
nombre,precio=carga()

#2) Imprimir los nombres y precios.
imprimir(nombre,precio)

#3) Imprimir el nombre de artículo con un precio mayor
mayor(nombre,precio)

#4) Ingresar por teclado un importe y luego mostrar todos los artículos  
# con un precio menor igual al valor ingresado
valor=int(input("Ingrese un valor de referencia para tomar menor igual :$"))
menor_teclado(valor,nombre,precio)

"""

nombre=["pepe","jorge"]
precio=[33,55]
print(nombre[0],"vale :$",precio[0])
"""