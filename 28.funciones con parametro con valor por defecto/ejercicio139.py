"""Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto."""

def suma(n1,n2,n3=0,n4=0,n5=0):
    sum=n1+n2+n3+n4+n5
    return sum

#main
print(suma(1,2,))

print(suma(77,88,99,22,11))