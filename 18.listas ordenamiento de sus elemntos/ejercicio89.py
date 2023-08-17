#Se debe crear y cargar una lista donde almacenar 5 sueldos. 
#Ordenar de menor a mayor la lista.
#Ahora bien como vimos en el problema anterior con los 4 elementos 
#que nos quedan podemos hacer el mismo proceso visto anteriormente, 
#con lo cual quedará ordenado otro elemento de la lista. 
#Este proceso lo repetiremos hasta que quede ordenado por completo la lista.
#Como debemos repetir el mismo algoritmo podemos englobar
# todo el bloque en otra estructura repetitiva.

lista=[]
for x in range (5):
    sueldo=int(input(" Ingrese el sueldo :"))
    lista.append(sueldo)

print("Lista ",lista)
for x in range (4):
    for y in range (4):
        if lista[y]>lista[y+1]:
            aux=lista[y+1]
            lista[y+1]=lista[y]
            lista[y]=aux
            
            
print("........")
print(lista)