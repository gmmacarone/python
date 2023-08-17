"""Elaborar una función que nos retorne el 
perímetro de un cuadrado pasando como parámetros el valor de un lado."""

def perimetro(lado):
    return (lado*4)

#main
lado=int(input("Ingrese lado :"))
print("El perimetro es ",perimetro(lado))