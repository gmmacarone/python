#Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
#Finalizar la carga de enteros al ingresar el cero. 
#Mostrar finalmente el tamaño de la lista.
lista=[]
num=int(input("Cargue el numero :"))
while num!=0:
    lista.append(num)
    num=int(input("Cargue el numero :"))
print("Se ingreso 0 , no se carga mas ",lista)
print("Tamaño ",len(lista))

