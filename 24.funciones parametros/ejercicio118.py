"""Desarrollar un programa que permita ingresar el lado de un cuadrado. 
Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
"""
   

def perimetro(lado):
    per=lado*4
    print("EL PERIMETRO ES ",per)

def superficie(lado):
    sup=lado*lado
    print("LA SUPERFICIE ES ",sup)

def carga():
    lado=int(input("Ingrese el lado en cm :"))
    eleccion=int(input("PARA PERIMETRO -1- PARA SUPERFICIE -2- :"))
    if eleccion==1:
        perimetro(lado)
    else:
        superficie(lado)

#main
carga()
