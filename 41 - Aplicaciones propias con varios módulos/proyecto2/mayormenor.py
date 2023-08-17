"""Confeccionar un módulo que implemente dos funciones, 
una que retorne el mayor de dos enteros y otra que retorne el menor de dos enteros.

En el módulo principal importar solo la función que retorne el mayor, 
luego cargar dos enteros y mostrar el mayor de ellos"""

def mayor(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
def menor(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2
    
