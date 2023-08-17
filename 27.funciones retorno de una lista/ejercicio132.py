"""Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. 
Desde el bloque principal del programa llamar a ambas funciones."""

def carga():
    lista=[]
    for i in range (5):
        num=int(input("Cargue los numeros :"))
        lista.append(num)
    return lista    

def mayores(lista):
    for i in range (5):
        if lista[i]>10:
            print ("Elementos mayores a 10 :",lista[i])

#main
mayores(carga())