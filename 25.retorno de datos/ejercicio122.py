"""Confeccionar una función que le enviemos como parámetro un string y nos 
retorne la cantidad de caracteres que tiene. 
En el bloque principal solicitar la carga de dos nombres por teclado y
 llamar a la función dos veces. 
Imprimir en el bloque principal cual de las dos palabras tiene más caracteres."""

def cant_letras(cadena):
    return len(cadena)

#main
nom1=input("Cargue primer nombre :")
nom2=input("Cargue segundo nombre :")

if cant_letras(nom1)>cant_letras(nom2):
    print("El primer nombre tiene mas letras ")
else:
    print("El segundo nombre tiene mas letras")