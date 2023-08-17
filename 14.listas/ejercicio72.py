#Definir por asignación una lista con 8 elementos enteros.
# Contar cuantos de dichos valores almacenan un valor superior a 100.
cont=0
enteros=[222,3,444,22,66666,4,6,77]
for x in range (len(enteros)):
    if enteros[x]>100:
        cont=cont+1
print ("lista   ",enteros)
print (" Mayores a 100 :",cont)