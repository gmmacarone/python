"""Almacenar en una lista 5 empleados, cada elemento de la lista 
es una sub lista con el nombre del empleado junto a sus últimos tres sueldos 
(estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral 
mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:

empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
"""


def carga():
    empleados=[]
    for i in range(5):
        nombre=input("Nombre del empleado :")
        sueldo_1=int(input("Ingrese primer sueldo : $"))
        sueldo_2=int(input("Ingrese segundo sueldo :$"))
        sueldo_3=int(input("Ingrese tercer sueldo :$"))
        empleados.append([nombre,(sueldo_1,sueldo_2,sueldo_3)])
    return (empleados)

def monto_total(empleados):
    lista_total=[]
    total=0    
    for i in range(5):
        total+=empleados[i][1][0]+empleados[i][1][1]+empleados[i][1][2]
        print("La plata del Empleado :",empleados[i][0],total)
        lista_total.append(total)
    #print(lista_total)
    return  lista_total

def ingresos_mayor(empleados,lista_total):
   for i in range(5):
    if lista_total[i]>10000:
        print("El empleado :",empleados[i][0]," supero los 10000 ",lista_total[i])
    

#main
empleados=carga()
lista_total=monto_total(empleados)
ingresos_mayor(empleados,lista_total)