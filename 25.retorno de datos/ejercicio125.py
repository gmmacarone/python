"""Confeccionar una función que calcule la superficie de un rectángulo y la retorne, 
la función recibe como parámetros los valores de dos de sus lados:
En el bloque principal del programa cargar los lados de dos rectángulos y 
luego mostrar cual de los dos tiene una superficie mayor."""


def superficie(lado1,lado2):
    return (lado1*lado2)

#main

lado_a=int(input("Cargue el lado uno "))
lado_b=int(input("Cargue el lado dos "))
sup1=superficie(lado_a,lado_b)
print("-------------OTRO RECTANGULO-----------")
lado_a=int(input("Cargue el lado uno "))
lado_b=int(input("Cargue el lado dos "))
sup2=superficie(lado_a,lado_b)

if sup1>sup2:
    print("Primer rectangulo , superficie mayor ",sup1)
else:
    print("Segundo rectangulo , superficie mayor ",sup2)


