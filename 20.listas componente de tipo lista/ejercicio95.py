#Crear una lista por asignación.
# La lista tiene que tener cuatro elementos. 
#Cada elemento debe ser una lista de 3 enteros.
#Imprimir sus elementos accediendo de diferentes modos.

lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista)
print("Tipo de impresion 1")
print(lista[0][0])
print(lista[0][1])
print(lista[0][2])
print("Tipo de impresion 2")
print(lista[0])
print(lista[1])
print(lista[2])
print("Tipo de impresion 3")
for y in range (len(lista[0])):
    print(lista[0][y])
print("Tipo de impresion 4")
for x in range(len(lista)):
    for y in range(len(lista[x])):
        print(lista[x][y])
