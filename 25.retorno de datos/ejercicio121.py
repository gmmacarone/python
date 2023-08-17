"""Confeccionar una función que le enviemos como parámetros dos enteros 
y nos retorne el mayor."""

def mayor(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
#main
ent1=int(input("Ingrese primer numero "))
ent2=int(input("Ingrese segundo numero "))
print("El mayor es :",mayor(ent1,ent2))
