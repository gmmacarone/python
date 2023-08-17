"""Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de 
empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga 
y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor."""


def carga():
    nom=input("Nombre del Empleado :")
    sal=int(input("Carga su salario :$"))
    return(nom,sal)

def mayor_salario(tupla1,tupla2):
    if tupla1[1]>tupla2[1]:
        print("El Empleado :",tupla1[0]," gana mas! $",tupla1[1])
    else:
        print("El Empleado :",tupla2[0]," gana mas! $",tupla2[1])

#main
tupla1=carga()
tupla2=carga()
mayor_salario(tupla1,tupla2)
