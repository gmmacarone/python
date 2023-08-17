"""Crear dos listas paralelas. En la primera ingresar los nombres de empleados
 y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo 
como su nombre)"""


nombre=[]
sueldos=[]

cant=int(input("Cuantos empleados cargamos?: "))

for i in range(cant):
    nom=input("Nombre del Empleado :")
    nombre.append(nom)
    plata=int(input("Ingrese el sueldo :$"))
    sueldos.append(plata)
print("-----------CARGA------------")

print(nombre)
print(sueldos)
pos=0
while pos<len(nombre):
    if sueldos[pos]>10000:
        sueldos.pop(pos)
        nombre.pop(pos)
    else:
        pos+=1
print("------------------ cambio -------------------")
print(nombre)
print(sueldos)
