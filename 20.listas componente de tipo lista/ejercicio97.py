#Crear una lista por asignación. La lista tiene que tener 5 elementos. 
#Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, 
#la segunda dos elementos, la tercera tres elementos y así sucesivamente.
#Sumar todos los valores de las listas.


lista=[[1],[2,3],[3,4,5],[4,5,6,7],[5,6,7,8,9]]
sum=0
for x in range (len(lista)):
    for y in range (len(lista[x])):
        sum=sum+lista[x][y]
print(lista)
print(sum)