#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado 
#y añadirlos a la lista. Imprimir la lista generada.

lista=[]
for x in range(5):
    num=int(input(" Cargue la lista :"))
    lista.append(num)
print (lista)