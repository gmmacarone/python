"""Desarrollar una función que reciba una lista de string y nos 
retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres 
debe retornar el que tiene un valor de componente más baja."""

def mas_caracteres(lista):
      
    for i in range (len(lista)-1):
        if len(lista[i])>len(lista[i+1]):
            indice=i
            
    print("El elemento con mas caracteres es ",lista[indice])
#main
lista=["juan","papatanasioplus","pedro","constantinoplanodejadeser!","pablo","jeremias"]
mas_caracteres(lista)