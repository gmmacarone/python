"""Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
Desde el bloque principal llamar dos veces a dicha funcion (sin utilizar
 una estructura repetitiva)"""


def carga_menor():
    num1=int(input("Carga el primero :"))
    num2=int(input("Carga el segundo :"))
    num3=int(input("Carga el tercero :"))
    if num1<num2 and num1<num3:
        print("El menor es ",num1)
    else:
        if num2<num1 and num2<num3:
            print ("El menor es ",num2)
        else:
            print("El menor es ",num3)
    
#main
carga_menor()
carga_menor()
