"""Desarrollar un programa que solicite la carga de 10 números
 e imprima la suma de los últimos 5 valores ingresados."""
sum=0
for x in range (10):
    num=int(input("Ingrese el numero :"))
    if x>=5:
        sum=sum+num
print ("la suma de los ultimos 5 numeros :",sum)
