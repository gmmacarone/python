"""Solicitar por teclado dos enteros. 
El primer valor indica la cantidad de elementos que crearemos en la lista. 
El segundo valor indica la cantidad de elementos que tendrá cada una de las listas 
internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.

Por ejemplo si el operador carga un 2 y un 4 significa que 
debemos crear una lista similar a:

"""
cant_list=int(input(" Cantidad de elementos que tendra la lista :"))
cant_int=int(input(" Cantidad de elementos que tendra ca una de las listas internas:"))

lista=[]
for x in range (cant_list):
    lista.append([])
    for y in range (cant_int):
        num=int(input("Ingrese el num :"))
        lista[x].append(num)
#muestro lista
print(lista) 

#muestro suma
sum=0
for x in range (len(lista)):
    for y in range (len(lista[x])):
        sum=sum+lista[x][y]
print(" La suma es :",sum)




