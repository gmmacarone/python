"""Confeccionar una función que reciba una serie de edades y me retorne 
la cantidad que son mayores o iguales a 18 
(como mínimo se envía un entero a la función)"""


def mayores(edad1,*edades):
    cant=0
    if edad1>18:
        cant+=1
    
    for i in range(len(edades)):
        if edades[i]>18:
            cant+=1
    return cant

#main

print("Cantidad mayores de 18")
print(mayores(12,3,44,55,6))