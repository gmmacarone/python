"""Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.

"""

import random

def carga():
    lista=[]
    for i in range (10):
        num=random.randint(0,1000)
        lista.append(num)
    return lista

def mostrar(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)
    return lista


#main
lista=carga()
mostrar(lista)
print("LISTA MEZCLADA !")
mezclar(lista)
mostrar(lista)