"""Definir una tupla con tres valores enteros. Convertir el contenido 
de la tupla a tipo lista. Modificar la lista y luego convertir
 la lista en tupla."""


def definir_tupla():
    num1=int(input("Ingrese el primer num:"))
    num2=int(input("Ingrese el segundo num:"))
    num3=int(input("Ingrese el tercer num:"))

    return (num1,num2,num3)

def convertir_a_lista(tupla):
    return list(tupla)

def modificar_lista(lista):
    print("La lista actual es :",lista)
    i=int(input("que indice desea modificar :"))
    new=int(input("El nuevo numero es :"))
    lista.pop(i)
    lista.insert(i,new)
    print("La lista modificada :",lista)
    return lista

def convertir_a_tupla(lista):
    return tuple(lista)

#main
tupla=definir_tupla()
lista=convertir_a_lista(tupla)
lista=modificar_lista(lista)
tupla=convertir_a_tupla(lista)
print("desde el MAIN")
print(lista)
print(tupla)
