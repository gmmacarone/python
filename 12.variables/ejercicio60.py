"""Realizar la carga de enteros por teclado.
 Preguntar después que ingresa el valor si desea cargar otro 
 valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados."""

opcion="si"
sum=0
while opcion=="si":
    n=int(input("Ingrese un valor :"))
    sum=sum+n
    opcion=input("Carga otro? si/no :")
print("La suma es ",sum)