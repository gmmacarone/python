#Crear y cargar dos listas con los nombres de 5 productos en una y 
#sus respectivos precios en otra. Definir dos listas paralelas. 
#Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

lista_producto=[]
lista_precio=[]

for x in range(5):
    producto=input(" Cargue el nombre del producto :")
    precio=int(input(" Cargue el precio :"))
    lista_producto.append(producto)
    lista_precio.append(precio)
cant=0
for x in range(5):
    if lista_precio[x]>lista_precio[0]:
        cant=cant+1

print(" Hay ",cant," productos con mayor precio de $",lista_precio[0])
