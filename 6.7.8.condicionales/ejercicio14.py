#Pedir tres notas a un alumno .Calcular el promedio y mostrar PROMOCIONADO >7 ; 
#REGULAR >= 4 y <7 y REPORBADO <4
#https://youtu.be/WjEq10yqtA0

nota1=int(input("Ingrese nota 1° :"))
nota2=int(input("Ingrese nota 2° :"))
nota3=int(input("Ingrese nota 3° :"))


prom=(nota1+nota2+nota3)/3
if(prom>7):
    print("Nota ",prom ,"PROMOCIONADO")
else:
    if (prom<4):
        print("Nota ",prom ,"REPROBADO")

    else:
        print("Nota ",prom ,"APROBADO")