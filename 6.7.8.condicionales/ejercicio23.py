#Se ingresa por teclado tres numeros, si al menos uno de ellos es < 10 
#debe aparecer un mensaje menor 10

num1=int(input(" Ingrese el primero :"))
num2=int(input("Ingrese el segundo  :"))
num3=int(input("Ingrese el tercerro :"))

if num1<10 or num2<10 or num3<10:
    print ("al menos UNO es 1 MENORES A 10")
else:
    print("NO todo es asi")