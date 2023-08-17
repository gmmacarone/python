#Escribir un programa que solicite ingresar 10 notas de alumnos y 
#nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
mayor=0
menor=0
alumno=1
while alumno<11:
    print("Nota del alumno" ,alumno)
    nota=int(input("Ingrese nota del alumno numero :"))
    alumno=alumno+1
    if nota>=7:
        mayor=mayor+1
    else:
        menor=menor+1

print("De un total de 10 alumnos , los de prom >7 :",mayor,"los de prom <7 :",menor)