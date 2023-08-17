#Una empresa tiene dos turnos (mañana y tarde)
# en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
#Confeccionar un programa que permita almacenar los sueldos de los empleados 
#agrupados en dos listas.
#Imprimir las dos listas de sueldos.

man=[]
tar=[]

for x in range(8):
    sueldo_man=int(input(" Ingrese sueldo del empleado TURNO MAÑANA :"))
    sueldo_tar=int(input(" Ingrese sueldo del empleado TURNO TARDE :"))
    man.append(sueldo_man)
    tar.append(sueldo_tar)
print("Lista MAÑANA",man)
print("Lista TARDE",tar)
