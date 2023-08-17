#Se ingresa por teclado tres numero , si todos los numeros son < 10 
#debe aparecer un mensaje TODOS  MENORES A 10

num1=int(input(" Ingrese el primero :"))
num2=int(input("Ingrese el segundo  :"))
num3=int(input("Ingrese el tercerro :"))

if num1<10 and num2<10 and num3<10:
    print ("TODOS MENORES A 10")
else:
    print("NO todo es asi")