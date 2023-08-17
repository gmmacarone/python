#Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos 
#tienen notas mayores o iguales a 7 y cuántos menores.
mayor=0
menor=0
for x in range(10):
    nota=int(input("Ingrese la nota :"))
    if nota>=7:
        mayor=mayor+1
    else:
        menor=menor+1
print(mayor," Tienen mas de 7 ",menor," Tienen menos de 7")