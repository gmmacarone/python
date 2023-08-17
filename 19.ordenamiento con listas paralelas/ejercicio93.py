#Confeccionar un programa que permita cargar los nombres de 5 alumnos 
#y sus notas respectivas. Luego ordenar las notas de mayor a menor. 
#Imprimir las notas y los nombres de los alumnos.
#Debe quedar claro que cuando intercambiamos las notas para dejarlas 
#ordenadas de mayor a menor debemos intercambiar los nombres para que las 
#listas continúen paralelas (es decir que en los mismos subíndices de cada
# lista continúe la información relacionada)

lista_alumno=[]
lista_nota=[]

for x in range (5):
    nombre=input("Ingrese nombre :")
    nota=int(input("Ingrese nota :"))
    lista_alumno.append(nombre)
    lista_nota.append(nota)

print (lista_alumno)
print(lista_nota)

for x in range (4):
    for y in range (4):
        if lista_nota[y]>lista_nota[y+1]:
            aux_nota=lista_nota[y+1]
            aux_nombre=lista_alumno[y+1]
            lista_nota[y+1]=lista_nota[y]
            lista_alumno[y+1]=lista_alumno[y]
            lista_nota[y]=aux_nota
            lista_alumno[y]=aux_nombre
print("---------------------")
print (lista_alumno)
print(lista_nota)