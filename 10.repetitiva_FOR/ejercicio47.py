"""Confeccionar un programa que lea n pares de datos, 
cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12."""
cant=0
n=int(input("Cuantos triangulos carga :"))
for x in range (n):
    base=int(input("Ingrese la base :"))
    altura=int(input("Ingrese la altura :"))
    print("CALCULAMOS")
    super=(base*altura)/2
    print("Del triangulo base :",base," Altura :",altura," Superficie :",super)
    if super>12:
        cant=cant+1
print("Los triangulos con Superficie > 12 ",cant)