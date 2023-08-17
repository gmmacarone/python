"""Se desea saber la temperatura media trimestral de cuatro paises. 
Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor."""


pais=[]
temp=[]
media=[]
#punto a)
for x in range (4):
    nombre=input("Ingrese el nombre del Pais :")
    pais.append(nombre)
    temp1=int(input("Ingrese la temperatura 1:"))
    temp2=int(input("Ingrese la temperatura 2:"))
    temp3=int(input("Ingrese la temperatura 3:"))
    temp.append([temp1, temp2, temp3])
#punto b)
print("--------------------")
print(pais)
print(temp)


#pais=["Chile","Bolivia","Peru","Brasil"]
#temp=[[3,40,20],[10,22,33],[223,545,4],[33,44,22]]
media=[]
#punto c)
acc=0
for x in range (4):
    for y in range (3):
        acc=acc+temp[x][y]
    prom=acc/3
    media.append(prom)
    prom=0
    acc=0
    print("--------------------")
    print(pais[x]," Temperatura media :",media[x])

#punto d)



for x in range (3):
    if media[x]>media[x+1]:
        aux=media[x+1]
        aux_pais=pais[x+1]
        media[x+1]=media[x]
        pais[x+1]=pais[x]
        media[x]=aux
        pais[x]=aux_pais
        
print("-----------------")
print(pais)
print(media)
print(" El Pais ",pais[3],"es el que tiene la temp mayor con ",media[3])

