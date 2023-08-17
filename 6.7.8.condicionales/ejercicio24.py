#Se ingresa por teclado tres numeros, si todos son = se suma num1+num2 el resultado x num3 

num1=int(input(" Ingrese el primero :"))
num2=int(input("Ingrese el segundo  :"))
num3=int(input("Ingrese el tercerro :"))

if num1==num2 and num1==num3:
    total=(num1+num2)*num3
    print ("TODOS IGUALES",total)
else:
    print("NO todo es asi")