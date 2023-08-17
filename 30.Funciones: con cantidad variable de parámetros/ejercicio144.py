"""Puede ser que tengamos una función que recibe una cantidad fija de parámetros y necesitemos llamarla enviando valores que se encuentran en una lista o tupla. La forma más sencilla es anteceder el caracter 
* al nombre de la variable:"""

def sumar(v1,v2,v3):
    suma=v1+v2+v3
    return suma

#main
lista=[1,2,3]
print(sumar(*lista))
#Con el caracter asterisco estamos haciendo que se descomponga la lista en sus tres elementos: