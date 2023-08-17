#Crear y cargar una lista con 5 enteros. 
#Implementar un algoritmo que identifique el mayor valor de la lista.

lista=[]
for x in range(5):
    num=int(input("Ingrese numero :"))
    lista.append(num)

compara=lista[0]
for x in range (1,5):
    if lista[x]>compara:
        compara=lista[x] 
print(lista)
print(compara)