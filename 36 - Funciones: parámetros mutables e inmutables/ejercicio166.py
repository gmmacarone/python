"""Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista"""

def carga():
    lista=[]
    for i in range(3):
        num=int(input("Cargue el numero :"))
        lista.append(num)
    return lista

def fijar(lista):
    for i in range (len(lista)):
        if lista[i]<10:
            lista[i]=0
    return lista
#main
lista=carga()
print("********* lista Original ****************")
print(lista)
lista=fijar(lista)
print("********* lista Modificada ****************")
print(lista)
