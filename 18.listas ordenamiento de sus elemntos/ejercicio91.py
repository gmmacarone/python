#Solicitar por teclado la cantidad de empleados que tiene la empresa. 
#Crear y cargar una lista con todos los sueldos de dichos empleados.
# Imprimir la lista de sueldos ordenamos de menor a mayor.

lista=[]
cant=int(input(" Cuantos empleados tiene :"))

for x in range (cant):
    sueldo=int(input(" Cargue el sueldo :"))
    lista.append(sueldo)
print(lista)

for x in range (cant-1):
    for y in range (cant-1):
        if lista[y]>lista[y+1]:
            aux=lista[y+1]
            lista[y+1]=lista[y]
            lista[y]=aux
print("---------------")
print(lista)
            
