#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. 
lista=[]
sum=0

for x in range(5):
    altura=float(input("Carga altura de la persona :"))
    lista.append(altura)
    sum=sum+altura
    prom=sum/5
print(" Las alturas son :",lista)
print(" los promedios ",prom)