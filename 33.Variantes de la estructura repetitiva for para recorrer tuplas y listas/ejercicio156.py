"""Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones:
1) Carga de empleados.
2) Impresión de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000."""


def carga():
    lista=[]
    for i in range(3):
        nombre=input("Ingrese nombre :")
        sueldo=int(input("Ingrese sueldo : $"))
        lista.append((nombre,sueldo))
    return lista

def impresion(lista):
    for elemento in lista:
        print(elemento[0],"__________$",elemento[1])


def nombre_mayor_sueldo(lista):
    mayor=lista[0][1]
    for elemento in lista:
        if elemento[1]>mayor:
            mayor=elemento[1]
            nombre=elemento[0]
    print("*******************")
    print("El que mas cobra ",nombre,"____$",mayor)

def menor(lista):
    count=0
    for elemento in lista:
        if elemento[1]<1000:
            count+=1
    print("Hay ",count,"empleados con sueldos menor a $1000")

#main
lista=carga()
impresion(lista)
nombre_mayor_sueldo(lista)
menor(lista)