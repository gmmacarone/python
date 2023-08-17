#Desarrollar un programa que permita cargar 5 nombres de personas 
#y sus edades respectivas. Luego de realizar la carga por teclado de todos 
#los datos imprimir los nombres de las personas mayores de edad 
#(mayores o iguales a 18 años)


#lista_nombres=["Juan","Pedro","Javi","Ester","Agu"]
#lista_edades=[8,33,55,2,66]

lista_nombres=[]
lista_edades=[]

for x in range(5):
    nombre=input(" Ingrese el nombre :")
    edad=int(input(" Ingrese la edad :"))
    lista_nombres.append(nombre)
    lista_edades.append(edad)

print(lista_nombres)
print(lista_edades)

for x in range(5):
    if lista_edades[x]>=18:
        print(lista_nombres[x]," tiene ",lista_edades[x])
