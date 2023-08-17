"""Confeccionar una función que reciba tres enteros y los muestre ordenados 
de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y 
proceder a llamar a la primer función definida."""

def orden(lista):
    comp=lista[0]
    for j in range (2):
        for i in range(2):
            if lista[i]>lista[i+1]:
                comp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=comp
    print("desde la funcion orden********")
    print(lista)
    for j in range(3):
        print(lista[j])

def carga():
    lista=[]
    for i in range(3):
        num=int(input("Ingrese el numero :"))
        lista.append(num)
    print("desde la funcion carga********")
    print(lista)
    orden(lista)

#main
carga()