#Crear y cargar una lista con los nombres de tres alumnos. 
#Cada alumno tiene dos notas, almacenar las notas en una lista paralela. 
#Cada componente de la lista paralela debe ser también una lista con las dos notas. 
#Imprimir luego cada nombre y sus dos notas.

alumnos=[]
notas=[]
for x in range (3):
    print("Se ingresa el alumno numero ",x)
    nombre=input("Nombre del alumno :")
    alumnos.append(nombre)
    print("Ingrese la nota del alumno ",alumnos[x] )
    nota1=int(input("Ingrese la nota 1 :"))
    nota2=int(input("Ingrese la nota 2 : "))
    notas.append([nota1,nota2])
for x in range (3):
    print(alumnos[x],notas[x][0],notas[x][1])   
print(alumnos)
print(notas)


