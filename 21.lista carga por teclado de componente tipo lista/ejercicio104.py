"""Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre
 de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de 
cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre."""


padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
hijos=[["marcos","alberto","silvia"], [], ["oscar"]]


for x in range (len(padres)):
    print("*****************************************************")
    print("La familia esta formada por ")
    print("Padre ",padres[x][0],"Madre ",padres[x][1])
    for y in range(len(hijos[x])):
        print("Los hijos son ",hijos[x][y])

print("*****************************************************")