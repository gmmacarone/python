"""Realizar la carga de dos nombres de personas distintos. 
Mostrar por pantalla luego ordenados en forma alfabética."""

nombre1=input("Ingrese su nombre ")
nombre2=input("Ingrese su nombre ")
if nombre1>nombre2:
    print(nombre2 , " y despues ",nombre1)
else:
    print(nombre1 , " y despues ",nombre2)