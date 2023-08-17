#Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.
sum=0
sueldos=[333.4,555.9,222,233,555,5]
for x in range(len(sueldos)):
    sum=sum+sueldos[x]
    prom=sum/5
print(" Los sueldos son ",sueldos)
print("El promedio ",prom)