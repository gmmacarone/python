""""Definir por asignación una lista de enteros en el bloque principal del programa.
 Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus 
 elementos, la segunda recibe la lista y retorna 
el mayor valor y la última recibe la lista y retorna el menor."""

def suma(lista):
    sum=0
    for i in range(len(lista)):
        sum=sum+lista[i]
    return sum

def mayor(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
    return lista.pop()

def menor(lista):
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
    return lista.pop()


#main
lista=[]
cant=int(input("Ingrese la cantidad de numeros :"))
for i in range(cant):
    num=int(input("Ingrese los numeros :"))
    lista.append(num)

print("LA suma es :",suma(lista))
print("El mayor es :",mayor(lista))
print("El menor es : ",menor(lista))