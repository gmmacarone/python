"""Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais 
y la cantidad de habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla 
y en la tercera mostrar
 el nombre del país con mayor cantidad de habitantes."""


def carga():
    lista_datos=[]
    for i in range(5):
        pais=input("Ingrese el Pais :")
        habi=int(input("Ingrese los habitantes :"))
        lista_datos.append((pais,habi))
    return(lista_datos)

def imprimir(lista):
    print("***************")
    print(lista)
    print("***************")

def mayor(lista):
    aux=lista[0][1]
    nombre=lista[0][0]
    for i in range(5):
        if lista [i][1]>aux:
            aux=lista[i][1]
            nombre=lista[i][0]
    print("El pais con más habitantes es :",nombre," posee :",aux)
#main
listado=carga()
imprimir(listado)
mayor(listado)