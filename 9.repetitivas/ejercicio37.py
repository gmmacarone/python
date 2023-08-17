#Realizar un programa que permita cargar dos listas de 15 valores cada una. 
#Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
acumulador_1=0
acumulador_2=0
x=0
while x<15:
    lista_1=int(input("Ingrese el valor lista 1:"))
    acumulador_1=acumulador_1+lista_1
    x=x+1
print("----------------------------------------------------------------")
x=0
while x<15:
    lista_2=int(input("Ingrese el valor lista 2:"))
    acumulador_2=acumulador_2+lista_1
    x=x+1

if acumulador_1==acumulador_2:
    print(" lista UNO  IGUAL a DOS",acumulador_1,"contra",acumulador_2)
else:    
    if acumulador_1>acumulador_2:
        print(" lista UNO MAYOR",acumulador_1,"contra",acumulador_2)
    else:
        print(" lista DOS MAYOR",acumulador_2,"contra",acumulador_1)