"""En un curso de 4 alumnos se registraron las notas de sus exámenes y se 
deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" 
si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

lista_nombre=[]
lista_nota=[]
lista_condicion=[]
cant=0
#carga
for x in range(4):
    nombre=input("Ingrese nombre ")
    nota=int(input("Ingrese nota :"))

    lista_nombre.append(nombre)
    lista_nota.append(nota)
#muestra
for x in range(4):
    print ("Nombre ",lista_nombre[x]," nota :",lista_nota[x])

#condicion
for x in range(4):
    if lista_nota[x]>=8:
        print("El alumno ",lista_nombre[x]," tiene MB")
        cant=cant+1
    else:
        if lista_nota[x]>=4 and lista_nota[x]<=7:
            print("El alumno ",lista_nombre[x]," tiene B")
        else:
            print("El alumno ",lista_nombre[x]," tiene I")  

#presenta
print(lista_nombre)
print(lista_nota)
print(lista_condicion)