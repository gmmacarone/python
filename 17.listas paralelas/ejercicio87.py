#Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos 
#cada una. Generar una tercer lista que surja de la suma de los elementos de la misma 
#posición de cada lista. Mostrar esta tercer lista.

lista_1=[]
lista_2=[]
lista_3=[]


for x in range (4):
    num1=int(input("Ingrese numero para lista 1 :"))
    lista_1.append(num1)
    num2=int(input("Ingrese numero para lista 2 :"))
    lista_2.append(num2)
    sum=lista_1[x]+lista_2[x]
    lista_3.append(sum)
    sum=0

print(" la lista es ",lista_3)