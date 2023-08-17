"""Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días."""

nombres=[]
faltas=[]

for x in range(3):
    nom=input("Ingrese el nombre :")
    nombres.append(nom)
    cant=int(input("Cuantos dias falto :"))
    faltas.append([])
    for y in range(cant):
        dia=int(input("Ingrese el dia! :"))
        faltas[x].append(dia)

print (nombres)
print(faltas)

#Cantidad de Inasistencias por empleado

for x in range(3):
    print(nombres[x] , "cantidad de inasistencias :",len(faltas[x]))


#Nombre de empleado y el/los dias que falto

for x in range(3):
    for y in range(len(faltas[x])):
        print (nombres[x]," falto ",faltas[x][y])


#nombre del que faltaron menos dias

men=len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<men:
        men=faltas[x]
        pos=x
print (nombres[pos], "falto ",men , " dias")