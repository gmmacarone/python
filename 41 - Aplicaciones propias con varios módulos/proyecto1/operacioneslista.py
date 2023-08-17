"""El módulo operacioneslista.py contiene todas las funciones que nos permiten cargar una lista, 
imprimir el mayor de una lista y sumar todos los elementos y mostrar dicho valor."""

def carga():
    lista=[]
    for i in range(5):
        num=int(input("Ingrese el numero a cargar en la lista :"))
        lista.append(num)
    return lista

def mayor(lista):
    may=lista[0]
    for i in range(4):
        if lista[i]>may:
            may=lista[i]
    print("EL MAYOR DE LA LISTA ES :",may)

def suma(lista):
    sum=0
    for i in range(5):
        sum+=lista[i]
    print("La suma de la lista :",sum)


    