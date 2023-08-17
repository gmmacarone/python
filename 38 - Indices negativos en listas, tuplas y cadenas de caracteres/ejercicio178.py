"""Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista"""


def carga():
    lista=[]
    for i in range (5):
        palabra=input("Ingrese la palabra :")
        lista.append(palabra)
    return lista

def intercambiar(lista):
    print("La Lista ORIGINAL es : ",lista)
    ultima=lista[-1]
    primera=lista[0]
    lista[0]=ultima
    lista[-1]=primera
    print("La lista MUTADA es :",lista)

def imprimir(lista):
    for i in range(5):
        print("********")
        print(lista[i])
#main
lista=carga()
intercambiar(lista)
imprimir(lista)