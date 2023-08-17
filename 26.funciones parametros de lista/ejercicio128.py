"""Crear y cargar por teclado en el bloque principal del programa una 
lista de 5 enteros. Implementar una función que imprima el mayor y el 
menor valor de la lista.

"""

def mayor_menor(lista):
    aux_mayor=lista[0]
    aux_menor=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>aux_mayor:
            aux_mayor=lista[i]
        else:
            aux_menor=lista[i]
    print("El mayor de la lista :",aux_mayor)
    print("El menor de la lista :",aux_menor)  
    



#main
lista=[]
for i in range (5):
    num=int(input("Cargue el numero :"))
    lista.append(num)
mayor_menor(lista) 