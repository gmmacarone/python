"""Plantear una función que reciba un string en mayúsculas o minúsculas 
y retorne la cantidad de letras 'a' o 'A'"""


def cuenta_vocal(cadena):
    cont=0
    for i in range (len(cadena)):
        if cadena[i]=="a" or cadena[i]=="A":
            cont+=1
    return cont

#main

palabra=input("Pase la palabra ! :")
cant=cuenta_vocal(palabra)
print("Tiene ",cant," a y A")