"""Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) 
valores enteros, retornar la suma de dichos parámetros."""

def sumar(v1,v2,*lista):
    sum=v1+v2
    for i in range(len(lista)):
        sum=sum+lista[i]
    return sum

#main

print("1+2")
print(sumar(1,2))
print("1+2+3+4")
print(sumar(1,2,3,4))
