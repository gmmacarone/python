"""Elaborar una función que reciba tres enteros y nos 
retorne el valor promedio de los mismos"""

def promedio(num1,num2,num3):
    return ((num1+num2+num3)/3)

#main
ent1=int(input("Ingrese el primero :"))
ent2=int(input("Ingrese el segundo :"))
ent3=int(input("Ingrese el tercero :"))

print("El promedio es :",promedio(ent1,ent2,ent3))
