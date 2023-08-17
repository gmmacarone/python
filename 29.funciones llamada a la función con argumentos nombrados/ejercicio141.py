"""Cargar una lista de 10 enteros, luego mostrarlos por pantalla a 
cada elemento separados por una coma."""

def carga():
    lista=[]
    for i in range(10):
        num=int(input("cargue el numero: "))
        lista.append(num)
    return lista

def muestra(lista):
    for i in range(10):

        print(lista[i],end=",")

#main
muestra(carga())