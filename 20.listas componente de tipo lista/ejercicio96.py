#Crear una lista por asignación. La lista tiene que tener 2 elementos.
# Cada elemento debe ser una lista de 5 enteros.
#Calcular y mostrar la suma de cada lista contenida en la lista 
#principal.

sum=0
lista=[[1,1,1,1,1],[2,2,2,2,2]]
for x in range (len(lista[0])):
    sum=sum+(lista[0][x])
print("La suma de la lista 0 es ",sum)
sum=0
for x in range (len(lista[1])):
    sum=sum+(lista[1][x])
print("La suma de la lista 1 es ",sum)
sum=0
for x in range (len(lista)):
    for y in range (len(lista[x])):
        sum=sum+(lista[x][y])
print("La suma de la lista es ",sum)
