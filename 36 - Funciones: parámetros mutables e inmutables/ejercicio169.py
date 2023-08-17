"""Crear un diccionario en Python para almacenar los datos de empleados
 de una empresa. La clave será su número de legajo y en su valor almacenar una 
 lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo 
para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"""


def carga():
    empleados={}
    for i in range (3):
        legajo=int(input("Ingrese legajo :"))
        nombre=input("Ingrese el nombre :")
        profesion=input("Ingrese profesion :")
        sueldo=int(input("Ingrese sueldo :$"))
        empleados[legajo]=[nombre,profesion,sueldo]
    return empleados

def mod_sueldo(empleados):
    legajo=int(input("Ingrese el legajo a modificar :"))
    if legajo in empleados:
        nuevo_sueldo=int(input("Actualice el sueldo ! :$"))
        empleados[legajo][2]=nuevo_sueldo
        print(empleados[legajo],empleados[legajo][0],empleados[legajo][1],empleados[legajo][2]) 
    else:
        print(" NO existe ese legajo!")

def mostrar_profesion_analista(empleados):
    print ("+++++++++++++++++++")
    print("Profesion ANA ")
    for legajo in empleados:
        if "ana"==empleados[legajo][1]:
            print(empleados[legajo]," : ",empleados[legajo][0], " ",empleados[legajo][1]," ",empleados[legajo][2]) 

#main
empleados=carga()
print(empleados)
mod_sueldo(empleados)
mostrar_profesion_analista(empleados)