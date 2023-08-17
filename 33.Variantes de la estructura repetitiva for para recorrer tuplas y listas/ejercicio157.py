"""Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas 
las palabras de la lista que tienen más de 5 caracteres."""

def carga():
    lista=[]
    palabra=input("Cargue palabra :")
    lista.append(palabra)
    return lista

def mostrar(lista):
    for elemento in lista:
        if len(elemento)>5:
            print("Palabras con mas de 5 letras :",elemento)

#main
lista=carga()
mostrar(lista)