"""Definir una lista de enteros por asignación en el bloque principal.
 Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
 Mostrar dicho producto en el bloque principal de nuestro programa."""

def producto(lista):
    prod=1
    for i in range (len(lista)):
        prod=prod*lista[i]
    return prod

#main
lista=[3,44,5,6,1]
print("El producto es :",producto(lista))
