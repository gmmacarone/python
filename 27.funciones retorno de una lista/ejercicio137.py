"""Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. 
En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas."""

def carga():
    lista=[]
    for i in range(10):
        num=int(input("Ingrese numero :"))
        lista.append(num)
    return lista

def genera(lista):
    pos=[]
    neg=[]
    for i in range(10):
        if lista[i]>=0:
            pos.append(lista[i])
        else:
            neg.append(lista[i])
    
    return[pos,neg]
   

#main
pos,neg=genera(carga())   
print("Lista de POSITIVOS ")
print(pos)
print("*************")  
print("Lista de NEGATIVOS")
print(neg)
