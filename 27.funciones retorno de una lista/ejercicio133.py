"""Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
 Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
 Desde el bloque principal del programa llamar a ambas 
funciones e imprimir el mayor y el menor de la lista."""


def carga():
    lista=[]
    for i in range(5):
        num=int(input("Ingrese el numero :"))
        lista.append(num)
    return lista    

def mayor_menor(lista):
    ma=lista[0]
    me=lista[0]
    for i in range(5):
        if lista[i]>ma:
            ma=lista[i]
        if lista[i]<me:
            me=lista[i]
    return[ma,me]
#main
lis=mayor_menor(carga())
print("El MAYOR :",lis[0])
print("El MENOR :",lis[1])