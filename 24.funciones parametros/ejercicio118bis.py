"""Desarrollar una funcion que reciba un string como parametro y nos muestre
 la cantidad de vocales. 
Llamarla desde el bloque principal del programa 3 veces con string distintos."""


def vocales(palabra):
    cont=0
    for i in range(len(palabra)):
        if palabra[i]=="a" or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u":
            cont+=1
    print(palabra," tiene ",cont," vocales")

#main
for i in range(3):
    palabra=(input(" Escriba la palabra : "))
    palabra_minuscula=palabra.lower()
    vocales(palabra_minuscula)
