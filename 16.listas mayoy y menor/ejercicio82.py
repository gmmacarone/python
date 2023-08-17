#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
#Mostrar el nombre de persona menor en orden alfabético.

lista=[]
for x in range(5):
    num=(input("Ingrese nombre :"))
    lista.append(num)

menor=lista[0]

for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        
print (lista)
print("MENOR ",menor)
