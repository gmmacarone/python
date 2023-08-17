"""Confeccionar un programa que solicite la carga de un valor 
entero por teclado y luego nos muestre la raíz cuadrada del número 
y el valor elevado al cubo.

Para resolver este problema utilizaremos dos funcionalidades que 
nos provee el módulo math de la biblioteca estándar de Python. 
Podemos consultar el módulo math """

from math import sqrt,pow
valor=int(input("Ingrese el numero :"))
raiz_cuadrada_valor=sqrt(valor)
cubo_valor=pow(valor,3)
print(" LA RAIZ CUADRADA de " , valor ," = ",raiz_cuadrada_valor)
print(" EL CUBO de ",valor," = ",cubo_valor)