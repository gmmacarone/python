#Definir una lista por asignación con 5 enteros. 
#Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista_num=[3,44,2,11,33]
for x in range (len(lista_num)):
    if lista_num[x]>=7:
        print ("los elementos > = 7 ")
        print (lista_num[x])
print (" De la lista ",lista_num)