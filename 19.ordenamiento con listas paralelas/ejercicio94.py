#Crear y cargar en un lista los nombres de 5 países y en otra lista paralela 
#la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir 
#los resultados. Por último ordenar con respecto a la cantidad de habitantes 
#(de mayor a menor) e imprimir nuevamente.

lista_pais=[]
lista_hab=[]

for x in range (5):
    nombre=input("Ingrese nombre Pais:")
    cant=int(input("Ingrese cantidad de habitantes :"))
    lista_pais.append(nombre)
    lista_hab.append(cant)

for x in range (5):
    print(lista_pais[x]," :",lista_hab[x])
print("--------------------")

#ordenado alfabeticamente 
for x in range (4):
    for y in range (4):
        if lista_pais[y]>lista_pais[y+1]:
            aux_pais=lista_pais[y+1]
            aux_hab=lista_hab[y+1]
            lista_pais[y+1]=lista_pais[y]
            lista_hab[y+1]=lista_hab[y]
            lista_pais[y]=aux_pais
            lista_hab[y]=aux_hab

for x in range (5):
    print(lista_pais[x]," :",lista_hab[x])

print("----------------------------------")

#ordenado por cantidad habitantes
for x in range (4):
    for y in range (4):
        if lista_hab[y]>lista_hab[y+1]:
            aux_pais=lista_pais[y+1]
            aux_hab=lista_hab[y+1]
            lista_pais[y+1]=lista_pais[y]
            lista_hab[y+1]=lista_hab[y]
            lista_pais[y]=aux_pais
            lista_hab[y]=aux_hab

for x in range (5):
    print(lista_pais[x]," :",lista_hab[x])


