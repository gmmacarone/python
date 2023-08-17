#Cargar una lista con 5 elementos enteros. 
#Imprimir el mayor y un mensaje si se repite dentro de la lista 
#Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje 
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 
#o más posiciones en la lista)
#(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

lista=[]
for x in range(5):
    num=int(input("Ingrese numero :"))
    lista.append(num)

mayor=lista[0]
comp=lista[0]
rep=0
for x in range (1,5):
    if lista[x]>mayor:
        mayor=lista[x]
    
for x in range (1,5):
    if mayor==lista[x]:
        rep=rep+1

if rep>1:
    print("Se mayor se aparece ",rep," veces")
    
print("El mayor numero es :",mayor)
