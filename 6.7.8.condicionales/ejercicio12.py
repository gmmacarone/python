#Se ingresan tres notas de un alumno si su promedio es mayor a siete sera promocionado

nota_1=int(input("Ingrese primera nota: "))
nota_2=int(input("Ingrese segunda nota: "))
nota_3=int(input("Ingrese tercera nota: "))
prom=(nota_1+nota_2+nota_3)/3
if prom>7:
    print("Alumno promociono con ",prom)
else:
    print("Alumno no promociono!",prom)
