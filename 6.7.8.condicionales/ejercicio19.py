"""
Condicionales compuestos con operadores lógicos
Identificar cual numeor es mayor de los tres

"""

num1=int(input(" Ingrese el primer numero :"))
num2=int(input(" Ingrese el segundo numero :"))
num3=int(input(" Ingrese el tercer numero :"))

if num1>num2 and num1>num3:
    print ("El ",num1, "Es el mayor")
else:
    if num2>num3:
        print ("El ",num2, "Es el mayor")
    else:
        print ("El ",num3, "Es el mayor")