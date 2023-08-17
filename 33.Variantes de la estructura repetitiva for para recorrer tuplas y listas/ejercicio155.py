"""Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto."""

def carga():
    lista=[]
    for i in range(5):
        num=int(input("Ingrese el numero :"))
        lista.append(num)
    return lista

def mayor(lista):
    aux=lista[0]
    for i in lista:
        if i>aux:
            aux=i
    print("*********************")
    print("MAYOR")
    print(aux)
    print("*********************")

def suma(lista):
    sum=0
    for i in lista:
        sum+=i
    print("*********************")
    print("SUMA")
    print(sum)
    print("*********************")

#main
lista=carga()
mayor(lista)
suma(lista)

