"""Realizar la carga por teclado del nombre, edad y altura de dos personas.
 Mostrar por pantalla el nombre de la persona con mayor altura."""

nombre1=input("ingrese el nombre :")
edad1=int(input("Ingrese la edad :"))
altura1=float(input("Ingrese la altura :"))

nombre2=input("ingrese el nombre :")
edad2=int(input("Ingrese la edad :"))
altura2=float(input("Ingrese la altura :"))

if altura1>altura2:
    print (" El hombre mas alto es ",nombre1)
else:
    print (" El hombre mas alto es ",nombre2)