"""Confeccionar un programa que permita cargar un código de producto 
como clave en un diccionario. Guardar para dicha clave el nombre del producto, 
su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero."""

def carga():
    productos={}
    for i in range (3):
        codigo=int(input("Ingrese el código NUMERICO del producto :"))
        nombre=input("Ingrese el nombre del producto :")
        precio=int(input("Ingrese el precio del producto :$"))
        cantidad=int(input("Ingrese cantidad de ese producto :"))
        productos[codigo]=(nombre,precio,cantidad)
    return productos

def lista_productos(productos):
    for claves in productos:
        print(claves,productos[claves][0],productos[claves][1],productos[claves][2])

def consulta_producto(productos):
    print()
    print("**************************")
    cod=int(input("Ingrese el CODIGO a buscar :"))
    if cod in productos:
        print(cod,productos[cod][0],productos[cod][1],productos[cod][2])

def stock_cero(productos):
    for claves in productos:
        if productos[claves][2]==0:
            print()
            print("**************************")
            print("Producto con CERO stock :")
            print(claves,productos[claves][0],productos[claves][1],productos[claves][2])
#main
productos=carga()
lista_productos(productos)
consulta_producto(productos)
stock_cero(productos)

