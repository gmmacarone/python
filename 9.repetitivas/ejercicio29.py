#Codificar un programa que solicite la carga de un valor positivo y nos muestre 
#desde 1 hasta el valor ingresado de uno en uno.
#Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30

num=int(input("Ingrese el valor maximo :"))
x=1
while x<=num:
    print(x)
    x=x+1
