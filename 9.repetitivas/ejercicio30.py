#Desarrollar un programa que permita la carga de 10 valores por teclado 
#y nos muestre posteriormente 
#la suma de los valores ingresados y su promedio.
x=0
sum=0
while x<10:
    valor=int(input("Ingrese el numero: "))
    sum=sum+valor
    prom=sum/10
    x=x+1
print("LA suma es ",sum , "El promedio es :",prom)