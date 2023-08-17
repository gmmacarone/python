#Cargar dos numeros.Si el primero es mayor , hacer suma y resta de ambos . Caso contrario producto y division
num1=int(input("Ingrese el primer numero :"))
num2=int(input("Ingrese el segundo numero :"))
if num1>num2:
    sum=num1+num2
    res=num1-num2
    print("La suma es",sum,"la resta es",res)
else:
    prod=num1*num2
    divi=num1/num2
    print("El producto es",prod,"la division es",divi)
