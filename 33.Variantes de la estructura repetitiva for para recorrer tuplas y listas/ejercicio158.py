"""Almacenar los nombres de 5 productos y sus precios. 
Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15."""

def carga():
    lista=[]
    for i in range(3):
        nombre=input("Nombre del producto :")
        precio=int(input("Precio del producto :"))
        lista.append((nombre,precio))
    return lista

def listar(lista):
    for nombre,precio in lista:
        print("Producto :",nombre,"_____$",precio)

def lista_rango(lista):
    for nombre,precio in lista:
        if precio>=10 and precio<=15:
            print("*****************")
            print("Los comprendidos entre $10 y $15")
            print("Producto :",nombre,"_____$",precio)
#main
lista=carga()
listar(lista)
lista_rango(lista)
