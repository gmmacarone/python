"""Crear una lista de enteros por asignación. Definir una función que 
reciba una lista de enteros y un segundo parámetro de tipo entero.
Dentro de la función mostrar cada elemento 
de la lista multiplicado por el valor entero enviado."""

def multiplicar(lista,factor):
    for i in range(len(lista)):
        producto=lista[i]*factor
        print("El producto es :",producto)
    print("******* lista original***********")
    print(lista)




#main
lista=[3,55,33,1,5]
print("__________ multiplicamos la lista por 3_____________")
multiplicar(lista,3)

