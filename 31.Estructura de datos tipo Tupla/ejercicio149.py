"""Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor."""

def carga():
    lista=[]
    for i in range(5):
        
        num=int(input("Carga el numero :"))
        lista.append(num)
    print(lista)    
    return lista

def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(5):
        
        if lista[x]>mayor:
            mayor=lista[x]
            
        else: 
            lista[x]<menor
            menor=lista[x]
            
   
    return(mayor,menor)

#main
lista=carga()
tupla=mayor_menor(lista)
mayor,menor=tupla
print(lista)
print("************")
print("El mayor es :",mayor)
print("El menor es :",menor)

