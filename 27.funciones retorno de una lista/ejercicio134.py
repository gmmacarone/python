"""Desarrollar un programa que permita cargar 5 nombres de personas
 y sus edades respectivas. Luego de realizar la carga por teclado de todos 
 los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas."""

def carga():
    nombres=[]
    edades=[]
    for i in range (5):
        nom=input("Ingrese el nombre :")
        ed=int(input("Ingrese la edad :"))
        nombres.append(nom)
        edades.append(ed)
    return[nombres,edades]

def mayores(nombres,edades):
    for i in range(5):
        if edades[i]>18:
            print("El usuario :",nombres[i])
            print("Tiene mas de 18 años , es mayor , tiene :",edades[i])
            print("***********")

def promedio(edades):
    sum=0
    for i in range (5):
        sum=sum+edades[i]
        prom=sum/5
    print("El promedio de edades :",prom)

#main

nombres,edades=carga()
mayores(nombres,edades)
promedio(edades)