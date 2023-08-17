"""Resolveremos el mismo problema anterior pero definiendo 
dos alias para las funciones sqrt y pow del módulo math."""

from math import sqrt as raiz , pow as elevar
valor=int(input("Ingrese el valor a operar ="))
resultado_raiz=raiz(valor)
resultado_potencia=elevar(valor,2)
print("Los resultados son ")
print("RAIZ ",resultado_raiz)
print("POTENCIA ",resultado_potencia)