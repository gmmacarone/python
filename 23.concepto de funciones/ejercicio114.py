"""Realizar un programa con dos funciones .La primer solicite el ingreso de un entero 
y muestre el cuadrado de dicho valor .La segunda que solicite la carga de dos valores 
y muestre el producto de los mismos . Llamar desde el bloque del programa principal
ambas funciones"""

def carga_entero():
    num=int(input("Ingrese un entero :"))
    cuadrado=pow(num,2)
    print(" El cuadrado de ",num," es :",cuadrado)

def carga_producto():
    num1=int(input("Ingrese el numero :"))
    num2=int(input("Ingrese el otro numero :"))
    producto=num1*num2
    print("El producto es ",num1,"x",num2,"=",producto)

#main

carga_entero()
carga_producto()