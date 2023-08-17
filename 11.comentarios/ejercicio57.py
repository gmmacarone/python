"""Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
Mostrar al final su suma. Definir varias líneas de comentarios indicando el
 nombre del programa, el programador y la fecha de la última modificación. 
Utilizar el caracter # para los comentarios."""

sum=0  #imicializo variable suma
for x in range (10):
    num=int(input("Carga el numero :"))
    sum=sum+num #sumo los valores
print (sum)