"""Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 
3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los 
últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado"""

empleados=[]
sueldos=[]
#punto a)
for x in range (3):
    nombre=input("Ingrese el nombre :")
    sueldo_1=int(input("Ingrese el primer sueldo :$"))
    sueldo_2=int(input("Ingrese el segundo sueldo :$"))
    sueldo_3=int(input("Ingrese el tercer sueldo :$"))
    empleados.append(nombre)
    sueldos.append([sueldo_1,sueldo_2,sueldo_3])
print(empleados)
print(sueldos)

#punto b)
sueldo_acc=[]
acc=0

for x in range (3):
    for y in range(3):
         acc=acc+sueldos[x][y]
    sueldo_acc.append(acc)
    acc=0
print(empleados)
print(sueldos)
print(sueldo_acc)

#punto c)
for x in range (3):
    print(empleados[x],"sueldo pagado en los ultimos 3 meses ",sueldo_acc[x])

#punto d)
print(empleados)
print(sueldo_acc)
if sueldo_acc[0]>sueldo_acc[1] and sueldo_acc[0]>sueldo_acc[2]:
    print("El mayor sueldo lo tuvo ",empleados[0])
else:
    if sueldo_acc[1]>sueldo_acc[2]:
        print("El mayor sueldo lo tuvo ",empleados[1])
    else:
        print("El mayor sueldo lo tuvo ",empleados[2])

#punto d) alternativa

print("---------------- ALTERNATIVA -------------------")
print(empleados)
print(sueldo_acc)

acc=sueldo_acc[0]
for x in range (1,3):
    if sueldo_acc[x]>acc:
        acc=sueldo_acc[x]
        pun=x
print("El mayor sueldo lo tiene ",empleados[x]," con $",acc)