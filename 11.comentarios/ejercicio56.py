"""Realizar un programa que solicite la carga de valores enteros por teclado 
y los sume. Finalizar la carga al ingresar el valor -1.
Dejar como comentario dentro del código fuente el enunciado del problema."""
n=0
sum=0
while (n!=-1):
    n=int(input(" Cargue el numero :"))
    sum=sum+n
print (sum) 