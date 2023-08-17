"""Confeccionar un programa que simule tirar dos dados y 
luego muestre los valores que salieron. Imprimir un mensaje que ganó si la suma 
de los mismos es igual a 7.
Para resolver este problema requerimos un algoritmo para que se genere un valor
 aleatorio entre 1 y 6. Como la generación de valores aleatorios es un tema muy 
 frecuente la biblioteca estándar de Python incluye un módulo que nos resuelve 
 la generación de valores aleatorios."""

import random

dado_1=random.randint(1,6)
dado_2=random.randint(1,6)
total=dado_1+dado_2
print("DADO 1 : ",dado_1)
print("DADO 2 :",dado_2)
if total==7:
    print("GANO!!")