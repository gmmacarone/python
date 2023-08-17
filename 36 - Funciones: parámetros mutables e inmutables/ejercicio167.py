"""Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres

"""


def carga():
    lista=[]
    for i in range (3):
        nombre=input("Cargue el nombre :")
        lista.append(nombre)
    return lista

def ordenar(lista):
    for i in range(3):
        for j in range(2):
            aux=lista[j]
            if aux>lista[j+1]:
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista

def imprimir(lista):
    for nombres in lista:
        print(nombres)
#main
lista=carga()

lista=ordenar(lista)
imprimir(lista)