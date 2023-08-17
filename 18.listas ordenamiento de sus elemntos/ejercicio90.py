#Crear una lista y almacenar los nombres de 5 países. 
#Ordenar alfabéticamente la lista e imprimirla

lista=[]
for x in range(5):
    pais=input(" Ingrese el Pais :")
    lista.append(pais)
aux=lista[0]

for y in range(4):
    for x in range (4):
        if lista[x]>lista[x+1]:
            aux=lista[x+1]
            lista[x+1]=lista[x]
            lista[x]=aux

print(lista)