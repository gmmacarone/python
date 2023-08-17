"""Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al 
generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó."""

import random

def genere():
    num=random.randint(1,5)
    return num

def adivina(num,num_oper):
    count=0
    while(num!=num_oper):
        if num>num_oper:
            print("El ALEATORIO es mayor que el tuyo!")
        else:
            print("El aleatorio es MENOR que el tuyo!")
        count+=1
        num_oper=int(input("Deci tu numero ! :"))
    print("SON IGUALES!!!!:::: GANOOOO", num,"=",num_oper)
    print("PROBO :",count)
 
        
#main
num=genere()
num_oper=int(input("Deci tu numero ! :"))

adivina(num,num_oper)