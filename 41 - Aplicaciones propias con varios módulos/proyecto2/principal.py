"""Confeccionar un módulo que implemente dos funciones, una que retorne el mayor de dos enteros y 
otra que retorne el menor de dos enteros.

En el módulo principal importar solo la función que retorne el mayor, 
luego cargar dos enteros y mostrar el mayor de ellos"""

from mayormenor import mayor

num1=int(input("Cargue el primer numero :"))
num2=int(input("Cargue el segundo numero :"))

maximo=mayor(num1,num2)
print("El mas grandote es :",maximo)