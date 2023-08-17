#Se cargan tres valores se calcule e 
#informe el rango de variacion (el mayor y el menor ingresado)

num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
num3=int(input("Ingrese el tercer numero:"))

if num1>num2 and num1>num3:
    mayor=num1
    if num2<num3:
        menor=num2
    else:
        menor=num3
    
else:
    if num2>num1 and num2>num3:
        mayor=num2
        if num3<num1:
            menor=num3
        else:
            menor=num1
    else:    
        if num3>num1 and num3>num2:
            mayor=num3
            if num1<num2:
                menor=num1
            else:
                menor=num2
print("RANGO . El mayor es:",mayor,"el menor es:",menor)