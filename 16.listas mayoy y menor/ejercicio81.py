#Crear y cargar una lista con 5 enteros por teclado. 
#Implementar un algoritmo que identifique el menor valor de la lista y 
#la posición donde se encuentra.

lista=[]
for x in range(5):
    num=int(input("Ingrese numero :"))
    lista.append(num)

menor=lista[0]
pos=0
for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        pos=x
print (lista)
print("MENOR ",menor)
print("POSICION ",pos)