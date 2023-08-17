"""Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores
 o iguales a 10 
y generar una nueva lista con dichos valores."""

lista=[]
lista_new=[]
for i in range(5):
    num=int(input("Ingrese un entero :"))
    lista.append(num)
print (lista)

count=0
while count<len(lista):
    if lista[count]>=10:
        mayor=lista.pop(count)
        lista_new.append(mayor)
    else:
        count+=1

print(lista_new)
print(lista)
