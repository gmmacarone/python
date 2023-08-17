#Cargar una lista con 5 elementos enteros. 
#Ordenarla de menor a mayor y mostrarla por pantalla, 
#luego ordenar de mayor a menor e imprimir nuevamente.

lista=[]
for x in range (5):
    num=int(input(" Carga el numero :"))
    lista.append(num)


for x in range (4):
    for y in range (4):
        if lista[y]>lista[y+1]:
            aux=lista[y+1]
            lista[y+1]=lista[y]
            lista[y]=aux

print(" Ordenado de menor a mayor")
print(lista)

for x in range (4):
    for y in range (4):
        if lista[y]<lista[y+1]:
            aux=lista[y+1]
            lista[y+1]=lista[y]
            lista[y]=aux

print(" Ordenado de mayor a menor ")
print(lista)
