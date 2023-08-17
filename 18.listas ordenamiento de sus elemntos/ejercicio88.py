
#Se debe crear y cargar una lista donde almacenar 5 sueldos. 
#Desplazar el valor mayor de la lista a la última posición.

lista=[]
for x in range (5):
    sueldo=int(input("Ingrese sueldo :"))
    lista.append(sueldo)
print (lista)

for x in range (4):
    if lista[x]>lista[x+1]:
        aux=lista[x]
        lista[x]=lista[x+1]
        lista[x+1]=aux
        
        
print("Lista ordenada)")
print(lista)