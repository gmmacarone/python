"""Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad 
(se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista."""

def carga_lista():
    lista=[]
    for i in range (10):
        num=int(input("Carga lista :"))
        lista.append(num)
    return lista

def mitad_lista(lista):
    mitad=int((len(lista)/2))
    #print("DESDE LA FUNCION ",mitad)
    primer_mitad=lista[:mitad]
    return primer_mitad

def impresiones(lista,primer_mitad):
    print("***** LISTA COMPLETA ****")
    print(lista)
    print("****** PRIMER MITAD *******")
    print(primer_mitad)

#main
lista=carga_lista()
primer_mitad=mitad_lista(lista)
impresiones(lista,primer_mitad)